import sqlite3

# Crear base de datos con puertas, usuarios y lasers
conn = sqlite3.connect("puertas.db")
cur = conn.cursor()

# Crear tabla de puertas
cur.execute("""
CREATE TABLE IF NOT EXISTS puertas (
    nombre TEXT PRIMARY KEY,
    abierta INTEGER DEFAULT 0
)
""")

# Crear tabla de usuarios (con campo codigo_rfid agregado)
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT PRIMARY KEY,
    dentro INTEGER DEFAULT 0,
    puede_abrir INTEGER DEFAULT 0,
    codigo_rfid TEXT UNIQUE
)
""")

# Crear tabla de lasers
cur.execute("""
CREATE TABLE IF NOT EXISTS lasers (
    nombre TEXT PRIMARY KEY,
    encendido INTEGER DEFAULT 0
)
""")

# Insertar puertas
cur.execute("INSERT OR IGNORE INTO puertas VALUES('puerta entrada', 0)")
cur.execute("INSERT OR IGNORE INTO puertas VALUES('puerta salida', 0)")

# Insertar usuarios con RFID
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('admin', 1, 1, 'AAA111')")
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('invitado', 0, 1, 'BBB222')")
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('Julieta', 0, 1, 'CCC333')")
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('Alen', 0, 1, 'DDD444')")
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('Pedro', 0, 1, 'EEE555')")
cur.execute("INSERT OR IGNORE INTO usuarios VALUES ('Santiago', 0, 1, 'FFF666')")

# Insertar lasers
cur.execute("INSERT OR IGNORE INTO lasers VALUES ('laser entrada', 0)")
cur.execute("INSERT OR IGNORE INTO lasers VALUES ('laser salida', 0)")

conn.commit()
conn.close()

print("Base de datos creada y poblada correctamente.")
