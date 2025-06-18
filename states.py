import flet as ft

puertas = {
    "Puerta Entrada": False,  # False = cerrada
    "Puerta Salida": False,  
}

lasers = {
    "Laser 1": False, #False = Laser apagado
    "Laser 2": False
}


def estado_puerta(nombre):
    if nombre in puertas:
        return "Abierta" if puertas[nombre] else "Cerrada"
    return "Desconocida"

def abrir_puerta(nombre):
    if nombre in puertas:
        puertas[nombre] = True
        print(f"{nombre} abierta.")
    else:
        print("Puerta no encontrada.")

def cerrar_puerta(nombre):
    if nombre in puertas:
        puertas[nombre] = False
        print(f"{nombre} cerrada.")
    else:
        print("Puerta no encontrada.")

def obtener_todas():
    return puertas


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

