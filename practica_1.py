""" Flet es GUI interfaces graficas de usuario 
flutter framework de google
"""

import flet as ft


def main(page: ft.Page):
    texto = ft.Text("MI primer app con flet")
    texto2 = ft.Text("segundo texto")
    page.title = "FLet app"
    page.bgcolor = ft.colors.GREEN_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cambiar_texto(e):
        texto2.value = "texto cambiado"
        page.update()

    boton = ft.FilledButton(text="Cambiar texto", on_click=cambiar_texto)
    page.add(texto, texto2, boton)


ft.app(target=main)
