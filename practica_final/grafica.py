import flet as ft
from logica import (
    init_db,
    get_books,
    get_favorites,
    add_book_to_db,
    add_to_favorites,
    delete_book_from_db,
)


def main(page: ft.Page):
    page.title = "Biblioteca personal"
    titulo = ft.Text("Biblioteca")
    init_db()

    def change_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        theme_icon_btn.icon = (
            ft.icons.DARK_MODE
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.icons.LIGHT_MODE
        )
        page.update()

    theme_icon_btn = ft.IconButton(
        icon=ft.icons.LIGHT_MODE, tooltip="Cambiar tema", on_click=change_theme
    )

    app_bar = ft.AppBar(
        title=titulo,
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[theme_icon_btn],
    )
    books_view = ft.ListView(expand=1, spacing=10, padding=20)
    wishlist_view = ft.ListView(expand=1, spacing=10, padding=20)

    # cargar libros desde la base de datos
    def load_books():
        books_view.controls.clear()
        for row in get_books():
            add_book_to_view(row[0], row[1], row[2])
        page.update()

    # cargar favoritos desde la base de datos
    def load_favorites():
        wishlist_view.controls.clear()
        for row in get_favorites():
            wishlist_view.controls.append(
                ft.ListTile(title=ft.Text(row[1]), subtitle=ft.Text(row[2]))
            )
        page.update()

    # añadir un libro a la vista
    def add_book_to_view(book_id, title, author):
        new_book = ft.ListTile(
            title=ft.Text(title),
            subtitle=ft.Text(author),
            trailing=ft.PopupMenuButton(
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        text="Eliminar",
                        on_click=lambda _: delete_book(book_id, new_book),
                    ),
                    ft.PopupMenuItem(
                        text="Añadir a favoritos",
                        on_click=lambda _: add_to_favorites_view(book_id),
                    ),
                ],
            ),
        )
        books_view.controls.append(new_book)

    # añadir un libro a la seccion de favoritos
    def add_to_favorites_view(book_id):
        add_to_favorites(book_id)
        load_favorites()

    # eliminar un libro de la vista
    def delete_book(book_id, book_control):
        delete_book_from_db(book_id)
        books_view.controls.remove(book_control)
        load_favorites()
        page.update()

    title_field = ft.TextField(label="Titulo del libro", width=300)
    author_field = ft.TextField(label="Autor del libro", width=300)
    add_button = ft.ElevatedButton("Añadir libro", on_click=lambda _: add_book())

    def add_book():
        if not title_field.value:
            title_field.error_text = "Por favor ingrese un titulo"
            page.update()
            return
        book_id = add_book_to_db(
            title_field.value, author_field.value or "Autor desconocido"
        )
        add_book_to_view(
            book_id, title_field.value, author_field.value or "Autor desconocido"
        )
        title_field.value = ""
        author_field.value = ""
        title_field.error_text = None
        page.update()

    add_book_view = ft.Column(
        [
            ft.Text("Añadir nuevo libro", size=20, weight=ft.FontWeight.BOLD),
            title_field,
            author_field,
            add_button,
        ],
        spacing=20,
    )

    def destination_change(e):
        index = e.control.selected_index
        content.controls.clear()
        if index == 0:
            content.controls.append(books_view)
        elif index == 1:
            content.controls.append(wishlist_view)
        elif index == 2:
            content.controls.append(add_book_view)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.BOOK, label="Libros"),
            ft.NavigationRailDestination(icon=ft.icons.FAVORITE, label="Favoritos"),
            ft.NavigationRailDestination(icon=ft.icons.ADD, label="Añadir libro"),
        ],
        on_change=destination_change,
    )
    content = ft.Column([books_view], expand=True)

    page.add(app_bar, ft.Row([rail, ft.VerticalDivider(width=1), content], expand=True))

    load_books()
    load_favorites()


ft.app(main)
