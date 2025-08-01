import flet as ft
import sqlite3
from states import *

def main(page: ft.Page):
    usuario_actual = "admin"
    page.title = "Sistema de Monitoreo"
    page.padding = 20
    page.window.width = 720
    page.window.height = 600

    # Contenedor principal
    contenido_area = ft.Container(
        content=ft.Text("Seleccioná una pestaña"),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(2),
        height=400,
        width=float('inf'),
        padding=10,
    )

    # --- Funciones de PUERTAS ---
    def manejar_click_puerta(nombre, abrir):
        if abrir:
            exito = abrir_puerta(nombre, usuario_actual)
        else:
            exito = cerrar_puerta(nombre, usuario_actual)

        if not exito:
            contenido_area.content = ft.Text("⚠️ No autorizado para controlar esta puerta.", size=18)
        else:
            mostrar_operaciones(None)
        page.update()

    def construir_contenido_puertas():
        lista_componentes = []
        for nombre, estado in obtener_todas().items():
            estado_texto = estado_puerta(nombre)
            texto_estado = ft.Text(f"{nombre.title()}: {estado_texto}", size=16)

            boton_abrir = ft.ElevatedButton(
                "Abrir",
                on_click=lambda e, n=nombre: manejar_click_puerta(n, True)
            )

            boton_cerrar = ft.ElevatedButton(
                "Cerrar",
                on_click=lambda e, n=nombre: manejar_click_puerta(n, False)
            )

            fila = ft.Row([texto_estado, boton_abrir, boton_cerrar], spacing=10)
            lista_componentes.append(fila)
        return ft.Column(lista_componentes)

    # --- Funciones de LASERS ---
    def manejar_click_laser(nombreLaser, prender):
        if prender:
            prender_laser(nombreLaser)
        else:
            apagar_laser(nombreLaser)
        mostrar_operaciones(None)

    def construir_contenido_lasers():
        lista_componentes_laser = []
        for nombre, estado in obtener_lasers().items():
            estado_laser_texto = estado_laser(nombre)
            texto_laser_estado = ft.Text(f"{nombre.title()}: {estado_laser_texto}", size=16)

            boton_prender = ft.ElevatedButton(
                "Encender",
                on_click=lambda e, n=nombre: manejar_click_laser(n, True)
            )

            boton_apagar = ft.ElevatedButton(
                "Apagar",
                on_click=lambda e, n=nombre: manejar_click_laser(n, False)
            )

            fila = ft.Row([texto_laser_estado, boton_prender, boton_apagar], spacing=10)
            lista_componentes_laser.append(fila)
        return ft.Column(lista_componentes_laser)

    # --- Vista de INGRESOS ---
    def construir_contenido_ingresos():
        dentro, fuera = obtener_usuarios_ingresos()

        columna_dentro = ft.Column([
            ft.Text(f"🟢 Ingresaron ({len(dentro)})", size=18, weight="bold"),
            ft.ListView([ft.Text(nombre) for nombre in dentro], spacing=5, height=250)
        ], expand=True)

        columna_fuera = ft.Column([
            ft.Text(f"🔴 No ingresaron ({len(fuera)})", size=18, weight="bold"),
            ft.ListView([ft.Text(nombre) for nombre in fuera], spacing=5, height=250)
        ], expand=True)

        fila = ft.Row(
            [columna_dentro, columna_fuera],
            spacing=50,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )

        boton_actualizar = ft.ElevatedButton(
            "🔄 Actualizar",
            on_click=lambda e: mostrar_ingresos(None),
            bgcolor=ft.Colors.GREEN_300,
            color=ft.Colors.BLACK
        )

        return ft.Column([
            fila,
            ft.Container(
                content=boton_actualizar,
                alignment=ft.alignment.center,
                padding=10
            )
        ])

    # --- Estado de botones seleccionados ---
    botones_estado = {
        "Ingresos": False,
        "Estados": False,
        "Operaciones": False
    }

    def actualizar_colores_botones():
        for boton in botones:
            nombre = boton.text
            seleccionado = botones_estado[nombre]
            boton.bgcolor = ft.Colors.BLUE_400 if seleccionado else ft.Colors.BLUE_200
            boton.color = ft.Colors.WHITE

    # --- Funciones para pestañas con selección ---
    def mostrar_ingresos(e):
        for k in botones_estado:
            botones_estado[k] = False
        botones_estado["Ingresos"] = True
        actualizar_colores_botones()
        contenido_area.content = construir_contenido_ingresos()
        page.update()

    def mostrar_estados(e):
        for k in botones_estado:
            botones_estado[k] = False
        botones_estado["Estados"] = True
        actualizar_colores_botones()
        contenido_area.content = ft.Text("Contenido de Estados", size=20)
        page.update()

    def mostrar_operaciones(e):
        for k in botones_estado:
            botones_estado[k] = False
        botones_estado["Operaciones"] = True
        actualizar_colores_botones()

        puertas = construir_contenido_puertas()
        lasers = construir_contenido_lasers()

        contenido_area.content = ft.Column([
            ft.Text("🔐 Control de Puertas", size=20, weight="bold"),
            puertas,
            ft.Divider(),
            ft.Text("🔦 Control de Lasers", size=20, weight="bold"),
            lasers
        ], spacing=20)
        page.update()

    # --- Crear botones y aplicarlos a la fila ---
    botones = [
        ft.ElevatedButton("Ingresos", on_click=mostrar_ingresos),
        ft.ElevatedButton("Estados", on_click=mostrar_estados),
        ft.ElevatedButton("Operaciones", on_click=mostrar_operaciones),
    ]
    actualizar_colores_botones()

    botones_menu = ft.Row(
        botones,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # --- Título principal ---
    titulo = ft.Text("Sistema de monitoreo", size=25, weight="bold", text_align="center")

    # --- Layout general ---
    page.add(
        ft.Column(
            [
                ft.Container(titulo, alignment=ft.alignment.center),
                botones_menu,
                contenido_area
            ],
            spacing=20,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Ejecutar en modo ventana
ft.app(target=main)
