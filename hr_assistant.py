"""
HR Assistant
Entry point of the application.
"""

import os

# ----------------------------------------------------
# Offline Mode
# ----------------------------------------------------

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

# ----------------------------------------------------
# Imports
# ----------------------------------------------------

from rich.console import Console
from rich.markdown import Markdown

from src.config import (
    SIMILARITY_THRESHOLD,
)

from src.document_loader import load_chunks

from src.vector_store import (
    build_vectorstore,
    get_context,
)

from src.memory import (
    load_memory,
    save_memory,
    add_memory,
    format_memory,
)

from src.prompt import PROMPT

from src.llm import generate

from src.utils import thinking

console = Console()


# ----------------------------------------------------
# Initialization
# ----------------------------------------------------

def initialize():
    """
    Initialize application.
    """

    console.print(
        "[bold green]🚀 Initializing HR Assistant...[/bold green]"
    )

    chunks = load_chunks()

    build_vectorstore(chunks)

    console.print(
        "[bold green]✅ Initialization complete.[/bold green]\n"
    )


# ----------------------------------------------------
# Chat Loop
# ----------------------------------------------------

def chat():

    history = load_memory()

    console.print(
        "[bold cyan]🧭 HR Assistant is ready![/bold cyan]"
    )

    console.print(
        "Type 'exit' to quit.\n"
    )

    while True:

        question = console.input(
            "[bold blue]You:[/bold blue] "
        ).strip()

        if not question:
            continue

        if question.lower() in (
            "exit",
            "quit",
        ):
            console.print(
                "[bold yellow]👋 Goodbye![/bold yellow]"
            )
            break

        thinking()

        # ----------------------------------------
        # Retrieve context
        # ----------------------------------------

        context, sources = get_context(question)

        if not sources:

            console.print(
                "[bold yellow]⚠ No relevant document found.[/bold yellow]\n"
            )

            continue

        best_score = min(
            source["score"]
            for source in sources
        )

        console.print(
            f"[dim]Similarity Score: {best_score:.4f}[/dim]"
        )

        # ----------------------------------------
        # Greeting detection
        # ----------------------------------------

        greetings = {
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        }

        if question.lower() in greetings:

            answer = (
                "Hello! 👋 I'm your HR Assistant.\n\n"
                "Feel free to ask me anything about the company policy, "
                "leave, attendance, benefits, working hours, reimbursement, "
                "or other HR-related topics."
            )

            console.print()

            console.print(
                "[bold magenta]HR Assistant[/bold magenta]"
            )

            console.print(
                Markdown(answer)
            )

            console.print()

            continue

        # ----------------------------------------
        # Similarity threshold
        # ----------------------------------------

        if best_score > SIMILARITY_THRESHOLD:

            console.print(
                "[bold yellow]⚠ I couldn't find a confident answer in the HR policy.[/bold yellow]"
            )

            console.print()

            continue

        # ----------------------------------------
        # Build Prompt
        # ----------------------------------------

        memory = format_memory(history)

        full_prompt = PROMPT.format(
            context=context,
            memory=memory,
            question=question,
        )

        # ----------------------------------------
        # LLM
        # ----------------------------------------

        answer = generate(
            full_prompt
        )

        # ----------------------------------------
        # Save Memory
        # ----------------------------------------

        history = add_memory(
            history,
            question,
            answer,
        )

        save_memory(history)

        # ----------------------------------------
        # Output
        # ----------------------------------------

        console.print()

        console.print(
            "[bold magenta]HR Assistant[/bold magenta]"
        )

        console.print(
            Markdown(answer)
        )

        console.print()

        console.print(
            "[bold cyan]📄 Sources[/bold cyan]"
        )

        shown = set()

        for source in sources:

            key = (
                source["source"],
                source["page"],
            )

            if key in shown:
                continue

            shown.add(key)

            console.print(
                f"• {source['source']} (Page {source['page'] + 1})"
            )

        console.print()


# ----------------------------------------------------
# Main
# ----------------------------------------------------

def main():

    initialize()

    chat()


if __name__ == "__main__":
    main()
