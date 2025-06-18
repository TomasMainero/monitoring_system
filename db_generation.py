import sqlite3

#Crear db con puertas, usuarios, y lasers

conn = sqlite3.connect("puertas.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS puertas (
    nombre TEXT PRIMARY KEY,
    abierta INTEGER DEFAULT 0            
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTs usuarios (
    nombre TEXT PRIMARY KEY,
    dentro INTEGER default 0,
    puede_abrir INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS lasers (
    nombre TEXT PRIMARY KEY,
    encendido INTEGER DEFAULT 0
)
""")

# agregar datos en puertas
cur.execute("""INSERT OR IGNORE INTO puertas VALUES('puerta entrada', 0)""")
cur.execute("""INSERT OR IGNORE INTO puertas VALUES('puerta salida', 0)""")

#agregar datos en usuarios
cur.execute("""INSERT OR IGNORE INTO usuarios VALUES ('admin', 1, 1)""")
cur.execute("""INSERT OR IGNORE INTO usuarios VALUES ('invitado', 0, 1)""")

#agregar datos en lasers
cur.execute("INSERT OR IGNORE INTO lasers VALUES ('laser entrada', 0)")
cur.execute("INSERT OR IGNORE INTO lasers VALUES ('laser salida', 0)")

conn.commit()
conn.close()