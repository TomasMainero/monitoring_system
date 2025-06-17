import sqlite3

def procesar_ingreso(codigo_rfid: str) -> int:
    resultado = 0  # por defecto: acceso denegado

    try:
        conn = sqlite3.connect("usuarios.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM usuarios WHERE codigo_rfid = ?", (codigo_rfid,))
        usuario = cur.fetchone()

        if usuario:
            cur.execute("UPDATE usuarios SET dentro = 1 WHERE codigo_rfid = ?", (codigo_rfid,))
            conn.commit()
            resultado = 1  # acceso autorizado

    finally:
        conn.close()

    return resultado

#Simulacion de ingreso de codigo RFID
codigo = input("Ingresá un código RFID: ")
resultado = procesar_ingreso(codigo)

if resultado == 1:
    print("Acceso autorizado")
else:
    print("Acceso denegado")