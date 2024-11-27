import flet as ft
import random


def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_900
    page.title = "Juego"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text("Cards, divider en flet", size=30, weight=ft.FontWeight.BOLD)

    numero_secreto = random.randint(1, 10)
    intentos = 0

    def verificar_intentos(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1
        if intento == numero_secreto:
            resultado.value = f"Correcto!! adivinaste en {intentos} intentos"
            resultado.color = ft.colors.GREEN
            verificar_btn.disabled = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado bajo, intente nuevamente"
            resultado.color = ft.colors.ORANGE
        else:
            resultado.value = "Demasiado alto, intente nuevamente"
            resultado.color = ft.colors.ORANGE
        intentos_text.value = f"Intentos: {intentos}"
        page.update()

    def reiniciar_juego(e):
        nonlocal numero_secreto, intentos
        numero_secreto = random.randint(1, 10)
        intentos = 0
        resultado.value = "Adivina el numero secreto entre 1 y 10"
        resultado.color = ft.colors.WHITE
        intentos_text.value = "Intentos 0"
        verificar_btn.disabled = False
        input_numero.value = "Tu intento"
        page.update()

    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.colors.GREY_50
            tema_btn.text = "Modo Oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.colors.GREY_900
            tema_btn.text = "Modo Claro"
        page.update()

    titulo_tema = ft.Text("Cambiar tema", size=20, weight=ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton("Modo Claro", on_click=cambiar_tema)

    input_numero = ft.TextField(label="Tu intento", width=100)
    verificar_btn = ft.ElevatedButton("Verificar", on_click=verificar_intentos)
    resultado = ft.Text("Adivina el numero secreto entre 1 y 10")

    intentos_text = ft.Text("Intentos: 0")
    reiniciar_btn = ft.ElevatedButton("Reiniciar juego", on_click=reiniciar_juego)

    card_1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [input_numero, verificar_btn, resultado, intentos_text, reiniciar_btn],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=10,
        ),
        width=300,
        height=400,
    )

    columna_tema = ft.Column(
        [titulo_tema, tema_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20
    )

    card_2 = ft.Card(
        content=ft.Container(
            content=columna_tema, alignment=ft.alignment.center, padding=10
        ),
        width=200,
        height=100,
    )

    divider_simple = ft.Divider(height=1, color=ft.colors.WHITE)
    divider_vertical = ft.VerticalDivider()

    layout = ft.Row(
        [card_1, divider_vertical, card_2], alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(titulo, divider_simple, layout)


ft.app(main)
