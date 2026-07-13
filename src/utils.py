"""
General utility functions.
"""

from time import sleep

from rich.console import Console

console = Console()


def thinking():
    """
    Display the thinking message.
    """

    console.print("[italic cyan]HR Assistant is thinking...[/italic cyan]")

    sleep(0.7)


def divider():
    """
    Print a divider line.
    """

    console.rule()
