import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = "App con filas y columnas"

    text_1 = ft.Text("texto 1", size=24, color=ft.colors.WHITE)
    text_2 = ft.Text("texto 2", size=24, color=ft.colors.WHITE)
    text_3 = ft.Text("texto 3", size=24, color=ft.colors.WHITE)

    text_row = ft.Row(
        [text_1, text_2, text_3], alignment=ft.MainAxisAlignment.CENTER, spacing=50
    )

    btn_1 = ft.FilledButton(text="boton 1")
    btn_2 = ft.FilledButton(text="boton 2")
    btn_3 = ft.FilledButton(text="boton 3")

    btn_row = ft.Row(
        [btn_1, btn_2, btn_3], alignment=ft.MainAxisAlignment.CENTER, spacing=30
    )

    text_col = [
        ft.Text("Columna 1 - fila 1", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 1 - fila 2", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 1 - fila 3", size=24, color=ft.colors.WHITE),
    ]

    text_col_1 = [
        ft.Text("Columna 2 - fila 1", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 2 - fila 2", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 2 - fila 3", size=24, color=ft.colors.WHITE),
    ]

    col_text_1 = ft.Column(text_col)
    col_text_2 = ft.Column(text_col_1)

    row_col = ft.Row(
        [col_text_1, col_text_2], alignment=ft.MainAxisAlignment.CENTER, spacing=50
    )
    page.add(row_col)


ft.app(main)
