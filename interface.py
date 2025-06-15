import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Monitoreo"
    page.padding = 20
    page.window_maximized = True

    # Contenido de cada pestaña
    contenido_ingresos = ft.Text("Contenido de Ingresos", size=20)
    contenido_estados = ft.Text("Contenido de Estados", size=20)
    contenido_operaciones = ft.Text("Contenido de Operaciones", size=20)

    # Contenedor que cambia según el botón presionado
    contenido_area = ft.Container(
        content=contenido_ingresos,  # inicial
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(2),
        height=400,
        width=float('inf'),
        padding=10,
    )

    # Funciones para cambiar el contenido
    def mostrar_ingresos(e):
        contenido_area.content = contenido_ingresos
        page.update()

    def mostrar_estados(e):
        contenido_area.content = contenido_estados
        page.update()

    def mostrar_operaciones(e):
        contenido_area.content = contenido_operaciones
        page.update()

    # Botones de navegación
    botones_menu = ft.Row(
        [
            ft.ElevatedButton("Ingresos", on_click=mostrar_ingresos),
            ft.ElevatedButton("Estados", on_click=mostrar_estados),
            ft.ElevatedButton("Operaciones", on_click=mostrar_operaciones)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Título
    titulo = ft.Text("Sistema de monitoreo", size=25, weight="bold", text_align="center")

    # Layout general
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

ft.app(target=main)
