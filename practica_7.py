import flet as ft
import random


def main(page: ft.Page):
    page.bgcolor = ft.colors.GREEN_200
    page.title = "Tabs en flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "Ejemplo de Pestañas",
        size=24,
        color=ft.colors.WHITE,
    )

    def generar_tareas():
        tareas = [
            "Estudiar python",
            "Aprender FLet",
            "Prepararse para el examen",
            "Hacer ejercicio",
            "Leer un libro",
            "Escuchar musica",
        ]
        return random.sample(tareas, 4)

    lista_tareas = ft.ListView(spacing=10, padding=20)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea, color=ft.colors.WHITE))
        page.update()

    actualizar_tareas()

    boton_actualizar = ft.ElevatedButton(
        "Actualizar tareas", on_click=lambda _: actualizar_tareas()
    )
    contenido_tareas = ft.Column([lista_tareas, boton_actualizar])

    # contenido pestaña perfil

    campo_nombre = ft.TextField(label="Nombre", bgcolor=ft.colors.GREEN_600)
    campo_email = ft.TextField(label="E-mail", bgcolor=ft.colors.GREEN_600)
    boton_guardar = ft.ElevatedButton("Guardar perfil")
    contenido_perfil = ft.Column([campo_nombre, campo_email, boton_guardar])

    # contenido configuracion
    switch_notificaciones = ft.Switch(label="Notificaciones", value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label="Volumen")
    contenido_configuracion = ft.Column([switch_notificaciones, slider_volumen])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Perfil", icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(
                text="Configuración",
                icon=ft.icons.SETTINGS,
                content=contenido_configuracion,
            ),
        ],
        expand=1,
    )

    page.add(titulo, tabs)


ft.app(main)
