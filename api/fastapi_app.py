import sqlite3
from sqlite3 import Error
from typing import List
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

def create_connection():
    """ Cria uma conexão com o banco de dados SQLite """
    conn = None
    try:
        conn = sqlite3.connect(str(Path(Path(__file__).parent.parent,
                                        "db/items.db")))
    except Error as e:
        print(e)
    return conn

def create_table():
    """ Cria a tabela de itens caso ela não exista """
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS items
                     (name TEXT, description TEXT, price REAL, tax REAL)''')
        conn.commit()
    finally:
        if conn:
            conn.close()

create_table()

@app.post("/items/")
async def create_item(item: Item):
    conn = create_connection()
    sql = '''INSERT INTO items(name, description, price, tax)
             VALUES(?,?,?,?)'''
    try:
        c = conn.cursor()
        c.execute(sql, (item.name, item.description, item.price, item.tax))
        conn.commit()
        return {"message": "Item criado com sucesso"}
    finally:
        if conn:
            conn.close()

@app.get("/items/", response_model=List[Item])
def read_items():
    conn = create_connection()
    items = []
    try:
        c = conn.cursor()
        for row in c.execute('SELECT name, description, price, tax FROM items'):
            items.append(Item(name=row[0], description=row[1], price=row[2], tax=row[3]))
        return items
    finally:
        if conn:
            conn.close()
