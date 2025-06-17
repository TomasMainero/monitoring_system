import sqlite3

conn = sqlite3.connect("usuarios.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    codigo_rfid TEXT UNIQUE NOT NULL,
    dentro INTEGER NOT NULL DEFAULT 0
)
""")

usuarios = [
    ("Juan", "123ABC", 0),
    ("María", "456DEF", 0),
    ("Pedro", "789GHI", 0),
    ("Lucía", "321JKL", 0)
]

cur.executemany("INSERT OR IGNORE INTO usuarios (nombre, codigo_rfid, dentro) VALUES (?, ?, ?)", usuarios)

conn.commit()
conn.close()
