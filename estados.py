puertas = {
    "Puerta Entrada": False,  # False = cerrada
    "Puerta Salida": False,  
}


def mostrar_estado(nombre):
    estado = puertas.get(nombre)
    if estado is None:
        print("Esa puerta no existe.")
    else:
        print(f"{nombre}: {'Abierta' if estado else 'Cerrada'}")

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
