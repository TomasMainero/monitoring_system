import flet as ft
import sqlite3

# Función para obtener listas de usuarios
def obtener_usuarios_ingresos():
    conn = sqlite3.connect("usuarios.db")
    cur = conn.cursor()
    
    cur.execute("SELECT nombre FROM usuarios WHERE dentro = 1")
    dentro = [r[0] for r in cur.fetchall()]
    
    cur.execute("SELECT nombre FROM usuarios WHERE dentro = 0")
    fuera = [r[0] for r in cur.fetchall()]
    
    conn.close()
    return dentro, fuera

def main(page: ft.Page):
    page.title = "Sistema de Monitoreo"
    page.padding = 20
    page.window_maximized = True

    # Contenedor principal
    contenido_area = ft.Container(
        content=ft.Text("Seleccioná una pestaña"),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(2),
        height=400,
        width=float('inf'),
        padding=10,
    )

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

        boton_actualizar = ft.ElevatedButton("Actualizar", on_click=lambda e: mostrar_ingresos(None))

        return ft.Column([
            fila,
            boton_actualizar
        ])

    # Funciones para pestañas
    def mostrar_ingresos(e):
        contenido_area.content = construir_contenido_ingresos()
        page.update()

    def mostrar_estados(e):
        contenido_area.content = ft.Text("Contenido de Estados", size=20)
        page.update()

    def mostrar_operaciones(e):
        contenido_area.content = ft.Text("Contenido de Operaciones", size=20)
        page.update()

    # Botones superiores
    botones_menu = ft.Row(
        [
            ft.ElevatedButton("Ingresos", on_click=mostrar_ingresos),
            ft.ElevatedButton("Estados", on_click=mostrar_estados),
            ft.ElevatedButton("Operaciones", on_click=mostrar_operaciones)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Título principal
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

# Ejecutar en modo ventana (no navegador)
ft.app(target=main)
