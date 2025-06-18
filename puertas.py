
puertas = {
    "puerta principal": False,  # False = cerrada
    "puerta trasera": False,
    "puerta del garaje": False
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

def main():
    while True:
        print("\nOpciones: mostrar, abrir, cerrar, salir")
        opcion = input("Elegí una opción: ").lower()
        if opcion == "salir":
            break
        elif opcion in ("mostrar", "abrir", "cerrar"):
            nombre = input("Nombre de la puerta: ")
            if opcion == "mostrar":
                mostrar_estado(nombre)
            elif opcion == "abrir":
                abrir_puerta(nombre)
            elif opcion == "cerrar":
                cerrar_puerta(nombre)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
