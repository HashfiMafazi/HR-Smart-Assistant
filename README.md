# 🤖 HR Assistant (Offline RAG with Ollama)

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

An offline Retrieval-Augmented Generation (RAG) HR Assistant powered by **Ollama**, **LangChain**, **FAISS**, and **HuggingFace Embeddings**.

</p>

---

## ✨ Features

* 🧠 Fully offline after initial setup
* 📄 Answer questions from HR policy PDFs
* 🔍 Semantic document search using FAISS
* 💬 Conversation memory
* ⚡ Lazy loading for faster startup
* 📦 Modular project architecture
* 🔒 Privacy-first (no cloud inference)
* 🖥️ Terminal-based interface
* 🚀 Easily extendable to multiple PDFs

---

## 📸 Preview

```text
🚀 Initializing HR Assistant...

📚 Found 1 PDF document(s).
📄 Loading employee_policy.pdf
✂ Created 9 chunks.
✅ Existing FAISS index found.

🧭 HR Assistant is ready!

You:
How many annual leave days do employees receive?

HR Assistant:

Employees are entitled to 12 days of annual leave after completing one year of service.

📄 Sources
• employee_policy.pdf (Page 2)
```

---

# 🏗 Architecture

```text
                User
                  │
                  ▼
          hr_assistant.py
                  │
                  ▼
        Document Loader (PDF)
                  │
                  ▼
      Recursive Text Splitter
                  │
                  ▼
        HuggingFace Embeddings
                  │
                  ▼
          FAISS Vector Store
                  │
                  ▼
            Context Retrieval
                  │
                  ▼
           Prompt Generation
                  │
                  ▼
           Ollama (Llama 3)
                  │
                  ▼
            Final Response
```

---

# 📁 Project Structure

```text
OLLAMAHRPROJECT/
│
├── hr_assistant.py
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── memory.py
│   ├── prompt.py
│   └── utils.py
│
├── documents/
│   └── employee_policy.pdf
│
├── faiss_index/
│
├── data/
│   └── conversation_memory.json
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Requirements

* Python 3.12+
* Ollama
* Git

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OLLAMAHRPROJECT.git

cd OLLAMAHRPROJECT
```

Create a virtual environment

```bash
python -m venv .venv
```

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the LLM

```bash
ollama pull llama3
```

---

# 📄 Add Your HR Policy

Place your PDF inside

```text
documents/
```

Example

```text
documents/
└── employee_policy.pdf
```

---

# ▶ Running

```bash
python hr_assistant.py
```

---

# 💬 Example

```text
You:
What is the company's working hour?

Assistant:
The standard working hours are Monday to Friday from 08:00 to 17:00.

Source:
employee_policy.pdf (Page 1)
```

---

# 🧠 Technologies

| Technology  | Purpose              |
| ----------- | -------------------- |
| Python      | Programming Language |
| LangChain   | RAG Framework        |
| Ollama      | Local LLM            |
| FAISS       | Vector Database      |
| HuggingFace | Embedding Model      |
| PyMuPDF     | PDF Loader           |
| Rich        | Terminal UI          |

---

# 🔒 Privacy

This project runs completely on your local machine.

Your documents are **never uploaded** to external servers after the required models have been downloaded and cached locally.

---

# 🛣 Roadmap

## ✅ Completed

* PDF loading
* Text chunking
* FAISS indexing
* Local embeddings
* Conversation memory
* Offline support
* Modular architecture

## 🚧 In Progress

* Multiple PDF support
* Better retrieval ranking
* Metadata filtering
* Source highlighting

## 🔮 Planned

* Web interface
* Streamed responses
* Hybrid search
* Citation improvements
* Docker support
* REST API
* Multi-user support

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

If you have suggestions for improvements, feel free to open an issue or submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Hashfi Mafazi**

Computer Science Student • IT Support • Software Engineer Enthusiast

If you find this project useful, consider giving it a ⭐ on GitHub.
