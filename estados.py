import flet as ft

puertas = {
    "Puerta Entrada": False,  # False = cerrada
    "Puerta Salida": False,  
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

   



