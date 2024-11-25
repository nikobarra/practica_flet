import flet as ft


def main(page: ft.Page):
    page.title = "Tablero Sticky Notes"
    page.bgcolor = ft.colors.GREY
    page.padding = 20
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # note = ft.TextField(value="Mi nota", multiline=True)

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def add_note(e):
        new_note = create_note("nueva nota")
        grid.controls.append(new_note)
        grid.update()

    title = ft.Text("Sticky notes", size=24, weight="bold", color=ft.colors.WHITE)
    add_btn = ft.IconButton(
        icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE
    )

    def create_note(text):
        note_content = ft.TextField(
            value=text,
            multiline=True,
            bgcolor=ft.colors.GREY_50,
        )

        note = ft.Container(
            content=ft.Column(
                [
                    note_content,
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda _: delete_note(note),
                    ),
                ]
            ),
            width=200,
            height=200,
            bgcolor=ft.colors.GREY_50,
            border_radius=10,
            padding=10,
        )
        return note

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
    )

    notes = [
        "nota 1",
        "nota 2",
        "nota 3",
    ]

    for note in notes:
        grid.controls.append(create_note(note))

    varios = ft.Row([title, add_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(varios, grid)


ft.app(main)
