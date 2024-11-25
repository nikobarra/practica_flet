import flet as ft  # Importa la librería Flet para crear la interfaz de usuario.


def main(page: ft.Page):
    # Configuración inicial de la página.
    page.title = "Tablero Sticky Notes"  # Establece el título de la ventana.
    page.bgcolor = ft.colors.GREY_800  # Asigna un color de fondo oscuro.
    page.padding = 20  # Define un espaciado de 20 píxeles en los bordes de la página.

    # Función para agregar una nueva nota.
    def add_note(e):
        new_note = create_note(
            "nueva nota"
        )  # Crea una nueva nota con texto predeterminado.
        grid.controls.append(new_note)  # Añade la nueva nota al contenedor GridView.
        grid.update()  # Refresca el GridView para mostrar la nota recién añadida.

    # Función para eliminar una nota del tablero.
    def delete_note(note):
        grid.controls.remove(note)  # Elimina la nota del contenedor GridView.
        page.update()  # Actualiza la página para reflejar los cambios.

    # Función para crear un contenedor de nota con un cuadro de texto y botón de eliminar.
    def create_note(text):
        # Crea un cuadro de texto inicializado con el texto especificado.
        note_content = ft.TextField(
            value=text,  # Texto inicial que mostrará la nota.
            multiline=True,  # Permite que el texto abarque varias líneas.
            bgcolor=ft.colors.GREY_50,  # Fondo claro para el cuadro de texto.
        )

        # Crea un contenedor para la nota que incluye el cuadro de texto y un botón de eliminar.
        note = ft.Container(
            content=ft.Column(
                [
                    note_content,  # El cuadro de texto donde se muestra el contenido de la nota.
                    ft.IconButton(
                        icon=ft.icons.DELETE,  # Botón con un icono de papelera.
                        on_click=lambda _: delete_note(
                            note
                        ),  # Asocia la acción de eliminar la nota.
                    ),
                ]
            ),
            width=200,  # Establece el ancho de la nota.
            height=200,  # Establece la altura de la nota.
            bgcolor=ft.colors.GREY_50,  # Fondo del contenedor de la nota.
            border_radius=10,  # Bordes redondeados para un diseño más agradable.
            padding=10,  # Espaciado interno dentro del contenedor.
        )
        return note  # Devuelve el contenedor de la nota.

    # Crea un GridView para organizar las notas.
    grid = ft.GridView(
        expand=True,  # El GridView ocupa todo el espacio disponible.
        max_extent=220,  # Define el ancho máximo de cada celda en el GridView.
        child_aspect_ratio=1,  # Mantiene una relación de aspecto 1:1 para las notas.
        spacing=10,  # Espaciado entre los elementos del GridView.
    )

    # Lista inicial de textos para las notas predeterminadas.
    notes = [
        "nota 1",  # Primer texto de nota.
        "nota 2",  # Segundo texto de nota.
        "nota 3",  # Tercer texto de nota.
    ]

    # Crea una nota por cada texto en la lista y la añade al GridView.
    for note in notes:
        grid.controls.append(create_note(note))

    # Título de la aplicación con estilo personalizado.
    title = ft.Text(
        "Sticky notes",  # Título del tablero.
        size=24,  # Tamaño del texto.
        weight="bold",  # Texto en negrita.
        color=ft.colors.WHITE,  # Color blanco para el texto.
    )

    # Botón para agregar una nueva nota al tablero.
    add_btn = ft.IconButton(
        icon=ft.icons.ADD,  # Icono de "Agregar".
        on_click=add_note,  # Asocia la acción de agregar una nueva nota.
        icon_color=ft.colors.WHITE,  # Color blanco para el icono.
    )

    # Añade el título, botón de agregar y el GridView a la página.
    page.add(
        ft.Row(
            [title, add_btn],  # Coloca el título y el botón en una fila.
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Los separa al inicio y al final de la fila.
        ),
        grid,  # Añade el GridView que contiene las notas.
    )


# Inicia la aplicación y ejecuta la función main como punto de entrada.
ft.app(target=main)
