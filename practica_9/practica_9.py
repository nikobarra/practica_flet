import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_800
    page.title = "Manejo de imagenes"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"

    texto_titulo = ft.Text(
        "Demo imagenes",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.GREY_200,
    )

    def create_example(title, description, content):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        title,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.GREY_200,
                    ),
                    ft.Text(description, color=ft.colors.GREY_300),
                    ft.Container(
                        content=content,
                        padding=10,
                        border=ft.border.all(1, ft.colors.GREY_400),
                    ),
                ]
            ),
            margin=ft.margin.only(bottom=20),
        )

    stack_ejemplo = ft.Stack(
        [
            ft.Container(width=200, height=200, bgcolor=ft.colors.GREY_900),
            ft.Container(
                width=150, height=150, bgcolor=ft.colors.GREY_700, left=25, top=25
            ),
            ft.Container(
                width=100, height=100, bgcolor=ft.colors.GREY_500, left=50, top=50
            ),
            ft.Text("Stack demo", color=ft.colors.WHITE, size=12, left=70, top=90),
        ],
        width=200,
        height=200,
    )

    stack_example = create_example(
        "stack", "stack nos permite superponer widgets", stack_ejemplo
    )

    # imagenes
    imagen_internet = ft.Image(src="https://picsum.photos/200/200", width=200)
    imagen_local = ft.Image(
        src="C:/Users/niko/Desktop/Python_Intermedio/clase_4/practica_9/assets/imagen.jpeg",
        width=200,
    )

    columna_imagen = ft.Column(
        [
            imagen_internet,
            ft.Text("Imagen desde URL", size=14, color=ft.colors.GREY_300),
            imagen_local,
            ft.Text(
                "imagen local (si esta disponible)", size=12, color=ft.colors.GREY_300
            ),
        ]
    )

    image_example = create_example(
        "Image", "Image permite mostrar imagenes", columna_imagen
    )

    # avatar
    imagen_avatar = ft.CircleAvatar(
        foreground_image_src="https://picsum.photos/200/200", radius=50
    )

    avatar_texto = ft.CircleAvatar(
        content=ft.Text("NMBP", color=ft.colors.GREY_800),
        radius=50,
        bgcolor=ft.colors.GREY_200,
    )
    fila = ft.Row([imagen_avatar, avatar_texto])
    circleavatar_example = create_example(
        "CircleAvatar", "Util para perfiles de usuario", fila
    )

    page.add(texto_titulo, stack_example, image_example, circleavatar_example)


ft.app(main)
