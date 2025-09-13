import sqlite3
from pathlib import Path

DB_PATH = Path("knowledge.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_entry(content: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO knowledge (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def list_entries():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, content FROM knowledge")
    rows = c.fetchall()
    conn.close()
    return rows

def query_entry(keyword: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, content FROM knowledge WHERE content LIKE ?", (f"%{keyword}%",))
    rows = c.fetchall()
    conn.close()
    return rows
