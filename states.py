import flet as ft
import sqlite3

puertas = {
    "Puerta Entrada": False,  # False = cerrada
    "Puerta Salida": False,  
}

lasers = {
    "Laser 1": False, #False = Laser apagado
    "Laser 2": False
}

def puede_abrir(usuario):
    conn = sqlite3.connect("puertas.db")
    cur = conn.cursor()
    cur.execute("SELECT puede_abrir FROM usuarios WHERE nombre = ?", (usuario,))
    resultado = cur.fetchone()
    conn.close()
    return resultado and resultado[0] == 1

def abrir_puerta(nombre_puerta, usuario):
    if not puede_abrir(usuario):
        return False #Usuario no autorizado, no puede abrir
    
    conn = sqlite3.connect("puertas.db")
    cur = conn.cursor()
    cur.execute("UPDATE puertas SET abierta = 1 WHERE nombre = ?", (nombre_puerta,))
    dentro, fuera = obtener_usuarios_ingresos()
    if usuario in dentro:
        cur.execute("UPDATE usuarios SET dentro = 0 WHERE nombre = ?", (usuario,))
    else:
        cur.execute("UPDATE usuarios SET dentro = 1 WHERE nombre = ?", (usuario,))
    conn.commit()
    conn.close()    
    return True

def cerrar_puerta(nombre_puerta, usuario):
    if not puede_abrir(usuario):
        return False #Usuario no autorizado, no puede abrir
    
    conn = sqlite3.connect("puertas.db")
    cur = conn.cursor()
    cur.execute("UPDATE puertas SET abierta = 0 WHERE nombre = ?", (nombre_puerta,))
    dentro, fuera = obtener_usuarios_ingresos()
    if usuario in dentro:
        cur.execute("UPDATE usuarios SET dentro = 0 WHERE nombre = ?", (usuario,))
    else:
        cur.execute("UPDATE usuarios SET dentro = 1 WHERE nombre = ?", (usuario,))
    conn.commit()
    conn.close()    
    return True

def estado_puerta(nombre_puerta):
    conn = sqlite3.connect("puertas.db")
    cur = conn.cursor()
    cur.execute("SELECT abierta FROM puertas WHERE nombre = ?", (nombre_puerta,))
    resultado = cur.fetchone()
    conn.close()
    if resultado:
        return "Abierta" if resultado[0] == 1 else "Cerrada"
    return "Desconocida"

def obtener_todas():
    conn = sqlite3.connect("puertas.db")
    cur = conn.cursor()
    cur.execute("SELECT nombre, abierta FROM puertas")
    datos = cur.fetchall()
    conn.close()
    return {nombre: abierta == 1 for nombre, abierta in datos}

# Función para obtener listas de usuarios
def obtener_usuarios_ingresos():
    conn = sqlite3.connect("puertas.db") # Conexión a la base de datos
    cur = conn.cursor()
    
    # Consulta usuarios que están dentro (dentro = 1)
    cur.execute("SELECT nombre FROM usuarios WHERE dentro = 1")
    dentro = [r[0] for r in cur.fetchall()] 
    
    # Consulta usuarios que están fuera (dentro = 0)
    cur.execute("SELECT nombre FROM usuarios WHERE dentro = 0")
    fuera = [r[0] for r in cur.fetchall()]
    
    conn.close()
    return dentro, fuera    


def estado_laser(nombre):
    if nombre in lasers:
        return "Activo" if lasers[nombre] else "Inactivo"
    return "Laser desconocido"

def prender_laser(nombre):
    if (nombre in lasers) and (lasers[nombre] == False):
        lasers[nombre] = True
        print(f"{nombre} prendido.")
    elif (lasers[nombre] == True):
        print(f"{nombre} ya esta prendido.")
    else:
        print(f"{nombre} no es válido.")

def apagar_laser(nombre):
    if (nombre in lasers) and (lasers[nombre] == True):
        lasers[nombre] = False
        print(f"{nombre} apagado.")
    elif (lasers[nombre] == False):
        print(f"{nombre} ya esta apagado.")
    else:
        print(f"{nombre} no es válido")

def obtener_lasers():
    return lasers

if __name__ == "__main__":
    usuario_test = "admin"
    puerta_test = "puerta entrada"

    print("Estado antes:", estado_puerta(puerta_test))
    exito = cerrar_puerta(puerta_test, usuario_test)
    print("Cierre exitoso?", exito)
    print("Estado después:", estado_puerta(puerta_test))