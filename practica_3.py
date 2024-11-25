# Importamos la librería Flet, que se utiliza para construir interfaces gráficas.
import flet as ft


# Definimos la función principal que se ejecutará al iniciar la aplicación.
def main(page: ft.Page):
    # Configuración inicial de la página principal.
    page.bgcolor = ft.colors.GREY  # Fondo gris para la página.
    page.title = "To Do App"  # Título de la ventana de la aplicación.
    page.horizontal_alignment = (
        ft.CrossAxisAlignment.CENTER
    )  # Centra los elementos horizontalmente.

    # Texto que actúa como título de la aplicación.
    app_title = ft.Text(
        "Lista de tareas con FLET",  # Texto del título.
        size=30,  # Tamaño de fuente grande.
        weight=ft.FontWeight.BOLD,  # Texto en negrita.
        color=ft.colors.WHITE,  # Color blanco para el texto.
    )

    # Función para agregar una tarea a la lista.
    def add_task(e):
        if input_task.value:  # Verifica si el cuadro de texto no está vacío.
            # Crea un elemento de la lista (ListTile) con un título y un checkbox.
            task = ft.ListTile(
                title=ft.Text(
                    input_task.value
                ),  # El título muestra el texto ingresado.
                leading=ft.Checkbox(
                    on_change=select_task
                ),  # Agrega un checkbox al inicio.
            )
            tasks.append(task)  # Añade la tarea a la lista de tareas.
            input_task.value = (
                ""  # Limpia el cuadro de texto después de agregar la tarea.
            )
            list_update()  # Actualiza la lista de tareas en la interfaz.

    # Función para manejar los cambios en los checkboxes (seleccionar tareas).
    def select_task(e):
        # Obtiene las tareas que están seleccionadas (checkbox marcado).
        selected = [t.title.value for t in tasks if t.leading.value]
        # Muestra las tareas seleccionadas en un texto debajo de la lista.
        selected_tasks.value = "Tareas seleccionadas: " + ", ".join(selected)
        page.update()  # Actualiza la página para reflejar los cambios.

    # Función para actualizar visualmente la lista de tareas.
    def list_update():
        tasks_list.controls.clear()  # Limpia todos los elementos actuales en la lista.
        tasks_list.controls.extend(
            tasks
        )  # Añade las tareas almacenadas a la lista visual.
        page.update()  # Actualiza la página para reflejar los cambios.

    # Cuadro de texto para ingresar una nueva tarea.
    input_task = ft.TextField(hint_text="Ingrese una tarea", filled=True)

    # Botón para agregar una nueva tarea.
    add_btn = ft.FilledButton(text="Agregar Tarea", on_click=add_task)

    # Lista para almacenar las tareas como objetos.
    tasks = []

    # Texto que muestra las tareas seleccionadas por el usuario.
    selected_tasks = ft.Text(
        "",  # Texto inicial vacío.
        size=20,  # Tamaño del texto más grande que el estándar.
        weight=ft.FontWeight.BOLD,  # Negrita para destacar.
        color=ft.colors.WHITE,  # Color blanco para el texto.
    )

    # Contenedor visual para mostrar las tareas como una lista con espacio entre elementos.
    tasks_list = ft.ListView(expand=1, spacing=3)

    # Añade todos los elementos a la página principal en orden.
    page.add(app_title, input_task, add_btn, tasks_list, selected_tasks)


# Inicia la aplicación ejecutando la función `main` como punto de entrada.
ft.app(target=main)
