import sqlite3

with sqlite3.connect('animal.db') as con:
    cur = con.cursor()
    query = """SELECT * FROM animal"""
    result = cur.execute(query)
    db = cur.fetchall(query)
    print(db)