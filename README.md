# mcp-sql-lite-demo

# MCP SQLite Knowledge Base

A simple **Model Context Protocol (MCP)** project built with **FastAPI** and **SQLite**.
This project allows you to store, retrieve, and query knowledge base entries via an API.

---

## 🚀 Features

* Store knowledge in a SQLite database.
* Retrieve and search notes via FastAPI endpoints.
* Built as a simple **MCP server** project.
* Easy to extend for embeddings, RAG, or AI-driven queries.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/mcp-sqlite-knowledge-base.git
cd mcp-sqlite-knowledge-base

pip install -r requirements.txt
```

---

## ▶️ Running the Server

Start the FastAPI server using:

```bash
python -m uvicorn server:app --reload
```

Server will run at:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
👉 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🗄️ Database Setup

The database is a simple **SQLite file** (`knowledge.db`).
To initialize and insert sample notes:

```python
import sqlite3

conn = sqlite3.connect("knowledge.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", ("AI Basics", "Artificial Intelligence is about building smart machines."))
cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", ("Python", "Python is widely used for AI and data science."))

conn.commit()
conn.close()
```

---

## 📖 API Endpoints

| Method | Endpoint                     | Description              |
| ------ | ---------------------------- | ------------------------ |
| POST   | `/add_note`                  | Add a new note to the DB |
| GET    | `/list_notes`                | List all notes           |
| GET    | `/search_notes?query=python` | Search notes             |

Example (with Swagger UI):
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠️ Tech Stack

* **Python 3.12+**
* **FastAPI**
* **SQLite**
* **Uvicorn**

---

## 🌱 Future Improvements

* Add embeddings + vector search.
* Integrate with LangChain or Graphiti.
* Build a frontend UI for browsing notes.

---

## 📜 License

MIT License

---

Do you want me to also include the **`requirements.txt`** inside the README for quick install, or keep it separate?
