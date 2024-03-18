import sqlite3
from flask import g

def connect_to_db():
    sql_db = sqlite3.connect("C:/Users/achuz/Documents/Coding-Projects/yag-todo/todo-app/todoapp.db")
    sql_db.row_factory = sqlite3.Row
    return sql_db

def get_db():
    if not hasattr(g, "todo_db"):
        g.todo_db = connect_to_db()
    return g.todo_db