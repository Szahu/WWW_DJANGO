from fastapi import FastAPI
import sqlite3
from typing import List

app = FastAPI()

@app.get("/tags")
async def read_tags():
    con = sqlite3.connect("db.sqlite3", check_same_thread=False)
    cur = con.cursor()
    query = "SELECT t.name AS tag_name, COUNT(pt.id) AS picture_count from obrazki_tag t LEFT JOIN obrazki_picture_tags pt ON t.id = pt.tag_id GROUP BY t.name"
    cur.execute(query)
    rows = cur.fetchall()
    data = [{'tag_name': row[0], 'picture_count': row[1]} for row in rows]
    return data

@app.get("/images")
async def read_images():
    con = sqlite3.connect("db.sqlite3", check_same_thread=False)
    cur = con.cursor()
    query = "SELECT p.id, p.name, t.name FROM obrazki_picture p LEFT JOIN obrazki_picture_tags pt ON p.id = pt.picture_id LEFT JOIN obrazki_tag t ON pt.tag_id = t.id"
    cur.execute(query)
    rows = cur.fetchall()
    data = [{'picture_id': row[0], 'picture_name': row[1], 'tags': row[2]} for row in rows]
    return data

@app.get("/images/{tag}")
async def read_images_by_tag(tag: str):
    con = sqlite3.connect("db.sqlite3", check_same_thread=False)
    cur = con.cursor()
    query = f"SELECT p.id, p.name FROM obrazki_picture p LEFT JOIN obrazki_picture_tags pt ON p.id = pt.picture_id LEFT JOIN obrazki_tag t ON pt.tag_id = t.id WHERE t.name = '{tag}'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    data = [{'picture_id': row[0], 'picture_name': row[1]} for row in rows]
    return data

@app.post("/images/del")
async def delete_images(ids: List[int]):
    con = sqlite3.connect("db.sqlite3", check_same_thread=False)
    cur = con.cursor()
    for id in ids:
        query = f"DELETE FROM obrazki_picture WHERE id = {id}"
        cur.execute(query)
    con.commit()
    return 'success'
