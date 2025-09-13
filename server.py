from fastapi import FastAPI
from db import init_db, add_entry, list_entries, query_entry
# server.py
app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello MCP with SQLite!"}


app = FastAPI(title="MCP SQLite Knowledge Base")

# Initialize DB
init_db()

@app.post("/add/")
def add(content: str):
    add_entry(content)
    return {"message": "✅ Entry added successfully"}

@app.get("/list/")
def list_all():
    rows = list_entries()
    return {"entries": rows}

@app.get("/query/")
def query(keyword: str):
    rows = query_entry(keyword)
    return {"results": rows}
