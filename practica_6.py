import flet as ft
from openpyxl import Workbook
from datetime import datetime


def main(page: ft.Page):
    page.title = "Datatable con excel"
    page.bgcolor = ft.colors.GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo = ft.Text("Datatable con Flet", size=24, color=ft.colors.WHITE)

    data_table = ft.DataTable(
        bgcolor=ft.colors.GREY_500,
        border=ft.border.all(2, ft.colors.GREY_100),
        border_radius=10,
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.colors.GREY_200)),
            ft.DataColumn(ft.Text("Nombre", color=ft.colors.GREY_200)),
            ft.DataColumn(ft.Text("Edad", color=ft.colors.GREY_200)),
        ],
        rows=[],
    )

    def guardar_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title = "Datos de la tabla en flet"
        ws.append(["ID", "Nombre", "Edad"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

            nombre_archivo = f"datos_tabla_{fecha_hora}.xlsx"

            wb.save(nombre_archivo)

            snack_bar = ft.SnackBar(
                content=ft.Text(f"Datos guardados en {nombre_archivo}")
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    def agregar_fila(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text(str(len(data_table.rows) + 1), color=ft.colors.WHITE)
                ),
                ft.DataCell(ft.Text(nombre_input.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.WHITE)),
            ]
        )
        data_table.rows.append(nueva_fila)
        nombre_input.value = ""
        edad_input.value = ""
        page.update()

    guardar_boton = ft.ElevatedButton(
        "Guardar en Excel",
        on_click=guardar_excel,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.GREEN,
    )

    nombre_input = ft.TextField(
        label="Nombre", bgcolor=ft.colors.GREY_700, color=ft.colors.WHITE
    )
    edad_input = ft.TextField(
        label="Edad", bgcolor=ft.colors.GREY_700, color=ft.colors.WHITE
    )

    agregar_boton = ft.ElevatedButton(
        "Agregar", on_click=agregar_fila, color=ft.colors.WHITE, bgcolor=ft.colors.BLUE
    )
    input_container = ft.Row(
        controls=[nombre_input, edad_input, agregar_boton, guardar_boton],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(titulo, data_table, input_container)


ft.app(main)
