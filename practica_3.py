import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY
    page.title = "TO DO App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    app_title = ft.Text(
        "Lista de tareas", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE
    )

    def add_task(e):
        if input_task.value:
            task = ft.ListTile(
                title=ft.Text(input_task.value),
                leading=ft.Checkbox(on_change=select_task),
            )
        tasks.append(task)
        input_task.value = ""
        list_update()

    def list_update():
        tasks_list.controls.clear()
        tasks_list.controls.extend(tasks)
        page.update()

    def select_task(e):
        selected = [t.title.value for t in tasks if t.leading.value]
        selected_task.value = "Tareas seleccionadas: " + ", ".join(selected)
        page.update()

    tasks_list = ft.ListView(expand=1, spacing=3)

    input_task = ft.TextField(hint_text="Ingrese una tarea", filled=True)
    add_btn = ft.FilledButton(text="Agregar tarea", on_click=add_task)
    tasks = []
    selected_task = ft.Text(
        "", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE
    )

    page.add(app_title, input_task, add_btn, tasks_list, selected_task)


ft.app(main)
