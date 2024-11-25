# Importa la librería Flet para crear interfaces gráficas y otros módulos necesarios
import flet as ft
import os  # Permite trabajar con rutas y el sistema de archivos
import base64  # Utilizado para codificar imágenes en base64


# Función para crear un producto con nombre, precio, color de fondo y una imagen
def crear_producto(nombre, precio, color, img_nombre):
    # Construye la ruta completa de la imagen a partir de la ubicación del script
    imagen_path = os.path.join(os.path.dirname(__file__), "assets", img_nombre)
    try:
        # Intenta abrir la imagen en modo binario y convertirla a base64
        with open(imagen_path, "rb") as image_file:
            imagen_bytes = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        # Si la imagen no se encuentra, imprime un mensaje de error
        print(f"Error: la imagen {img_nombre} no existe en {imagen_path}")
        imagen_bytes = None  # Define la imagen como nula si no existe

    # Devuelve un contenedor que representa un producto
    return ft.Container(
        content=ft.Column(  # Columna que contiene los elementos del producto
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
        bgcolor=color,  # Color de fondo del contenedor
        border_radius=10,  # Bordes redondeados
        padding=20,  # Espaciado interno
        alignment=ft.alignment.center,  # Alineación del contenido al centro
    )


# Función principal para construir la interfaz de la aplicación
def main(page: ft.Page):
    # Configura el título de la página
    page.title = "Galeria Responsive en FLET"
    # Define el tema oscuro de la aplicación
    page.theme_mode = ft.ThemeMode.DARK
    # Establece el color de fondo de la página
    page.bgcolor = ft.colors.GREY_800

    # Lista de productos, cada uno creado con la función `crear_producto`
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

    # Crea una fila responsiva para organizar los productos
    galeria = ft.ResponsiveRow(
        [
            # Cada producto se coloca dentro de un contenedor con diseño responsivo
            ft.Container(producto, col={"sm": 12, "md": 6, "lg": 3})
            for producto in productos
        ],
        run_spacing=20,  # Espaciado vertical entre las filas
        spacing=20,  # Espaciado horizontal entre columnas
    )

    # Crea una columna que contiene el título, un divisor y la galería
    contenido = ft.Column(
        [
            ft.Text(
                "Galeria de productos", size=32, weight=ft.FontWeight.BOLD
            ),  # Título
            ft.Divider(height=20, color=ft.colors.WHITE24),  # Divisor decorativo
            galeria,  # Galería de productos
        ],
        scroll=ft.ScrollMode.AUTO,  # Permite desplazamiento vertical
        expand=True,  # Expande la columna para llenar la página
    )
    # Agrega el contenido a la página
    page.add(contenido)


# Ejecuta la aplicación pasando la función principal
ft.app(main)
