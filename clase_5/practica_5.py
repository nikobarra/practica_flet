import flet as ft
import os
import base64


def main(page: ft.Page):
    page.title = "Galeria en flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.GREY_800

    def crear_producto(nombre, precio, color, img_nombre):
        imagen_path = os.path.join(os.path.dirname(__file__), "assets", img_nombre)
        try:
            with open(imagen_path, "rb") as image_file:
                imagen_bytes = base64.b64encode(image_file.read()).decode()
        except FileNotFoundError:
            print(f"error: la imagen {img_nombre} no existe en {imagen_path}")
            imagen_bytes = None

        return ft.Container(
            content=ft.Column(
                [
                    # Imagen del producto codificada en base64
                    ft.Image(
                        src_base64=imagen_bytes,  # Imagen codificada
                        width=150,  # Ancho de la imagen
                        height=150,  # Alto de la imagen
                        fit=ft.ImageFit.CONTAIN,  # Ajusta la imagen sin recortarla
                        error_content=(  # Contenido mostrado si ocurre un error con la imagen
                            ft.Text("Imagen no encontrada")
                            if imagen_bytes
                            else ft.Text("Imagen no encontrada")
                        ),
                    ),
                    # Nombre del producto
                    ft.Text(nombre, size=16, weight=ft.FontWeight.BOLD),
                    # Precio del producto
                    ft.Text(precio, size=14),
                    # Botón para agregar al carrito
                    ft.ElevatedButton("Agregar al carrito", color=ft.colors.WHITE),
                ]
            ),
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
        )

    productos = [
        crear_producto(
            "Producto 1", "10.99", ft.colors.RED_500, img_nombre="car_1.png"
        ),
        crear_producto(
            "Producto 2", "9.99", ft.colors.GREEN_500, img_nombre="car_2.png"
        ),
        crear_producto(
            "Producto 3", "12.99", ft.colors.BLUE_500, img_nombre="car_3.png"
        ),
        crear_producto(
            "Producto 4", "8.99", ft.colors.ORANGE_500, img_nombre="car_4.png"
        ),
        crear_producto(
            "Producto 5", "87.99", ft.colors.GREEN_800, img_nombre="car_5.png"
        ),
        crear_producto(
            "Producto 6", "82.99", ft.colors.BLUE_GREY_300, img_nombre="car_6.png"
        ),
        crear_producto(
            "Producto 7", "81.99", ft.colors.PINK_400, img_nombre="car_7.png"
        ),
        crear_producto(
            "Producto 8", "89.99", ft.colors.RED_ACCENT_100, img_nombre="car_8.png"
        ),
    ]

    galeria = ft.ResponsiveRow(
        [
            ft.Container(producto, col={"sm": 12, "md": 6, "lg": 3})
            for producto in productos
        ],
        run_spacing=20,
        spacing=20,
    )

    contenido = ft.Column(
        [
            ft.Text("Galeria de productos", size=32, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20, color=ft.colors.WHITE24),
            galeria,
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    page.add(contenido)


ft.app(main)
