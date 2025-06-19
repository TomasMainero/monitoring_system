import sqlite3

def procesar_ingreso(codigo_rfid: str) -> int:
    resultado = 0  # por defecto: acceso denegado

    try:
        conn = sqlite3.connect("puertas.db")
        cur = conn.cursor()

        cur.execute("SELECT nombre FROM usuarios WHERE codigo_rfid = ?", (codigo_rfid,))
        usuario = cur.fetchone()

        if usuario:
            # Alternar estado dentro
            cur.execute("SELECT dentro FROM usuarios WHERE codigo_rfid = ?", (codigo_rfid,))
            dentro_actual = cur.fetchone()[0]
            nuevo_estado = 0 if dentro_actual == 1 else 1

            cur.execute("UPDATE usuarios SET dentro = ? WHERE codigo_rfid = ?", (nuevo_estado, codigo_rfid))
            conn.commit()
            resultado = 1  # acceso autorizado

    finally:
        conn.close()

    return resultado

# Simulación
codigo = input("Ingresá un código RFID: ")
resultado = procesar_ingreso(codigo)

if resultado == 1:
    print("Acceso autorizado")
else:
    print("Acceso denegado")
