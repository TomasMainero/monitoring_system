import sqlite3

# Crear base de datos de usuarios
conn = sqlite3.connect("usuarios.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT PRIMARY KEY,
    dentro BOOLEAN
)
""")
conn.commit()
conn.close()

# Crear base de datos de estados
conn = sqlite3.connect("estados.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS estados (
    puertaEntrada TEXT,
    estadoEntrada BOOLEAN,
    puertaSalida TEXT,
    estadoSalida BOOLEAN,
    laser TEXT,
    estadoLaser BOOLEAN
)
""")
# Insertar un estado inicial si la tabla está vacía
cur.execute("SELECT COUNT(*) FROM estados")
if cur.fetchone()[0] == 0:
    cur.execute("""
    INSERT INTO estados (puertaEntrada, estadoEntrada, puertaSalida, estadoSalida, laser, estadoLaser)
    VALUES (?, ?, ?, ?, ?, ?)
    """, ("Puerta Entrada", 0, "Puerta Salida", 0, "Laser 1", 0))
conn.commit()
conn.close()
