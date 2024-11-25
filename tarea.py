""" Gestión de Tareas Pendientes
Crea un programa en Python que permita gestionar una lista de tareas pendientes utilizando una base de datos y aplicando el paradigma orientado a objetos. El programa debe incluir las operaciones básicas de un CRUD (Crear, Leer, Actualizar y Eliminar) para las tareas.

Cada tarea debe tener los siguientes atributos:

ID (autogenerado): identificador único de cada tarea.
Descripción: un texto breve que describa la tarea.
Estado: puede ser "Pendiente" o "Completada".
Fecha límite: la fecha en la que se debe completar la tarea (opcional).
El programa debe tener un menú interactivo que permita realizar las siguientes acciones:

Crear una nueva tarea.
Listar todas las tareas.
Marcar una tarea como "Completada".
Actualizar la descripción o la fecha límite de una tarea.
Eliminar una tarea.
Salir del programa.
Requisitos Técnicos
Usa una base de datos SQLite para almacenar las tareas.
Representa cada tarea como un objeto de una clase Tarea.
Cada operación del CRUD debe interactuar con la base de datos y manipular objetos Tarea.
Agrega validaciones para garantizar que:
El estado solo sea "Pendiente" o "Completada".
Las tareas tengan una descripción no vacía.
Las fechas sean opcionales pero válidas si se ingresan.
Implementa un menú interactivo que funcione en bucle hasta que el usuario elija salir.
Pasos para Resolver el Ejercicio
Definir la clase Tarea:

Incluye un constructor para inicializar una tarea con sus atributos.
Implementa un método __str__ para mostrar la tarea en formato legible.
Configurar la base de datos:

Crea una base de datos SQLite llamada tareas.db.
Define una tabla tareas con columnas para ID, descripción, estado y fecha límite.
Implementar funciones para las operaciones CRUD:

Crear una tarea: Solicita al usuario la descripción y la fecha límite. Inserta la nueva tarea en la base de datos con estado "Pendiente".
Leer todas las tareas: Recupera y muestra todas las tareas de la base de datos, indicando su ID, descripción, estado y fecha límite.
Actualizar una tarea: Permite modificar la descripción o la fecha límite de una tarea existente usando su ID.
Cambiar el estado: Marca una tarea como "Completada" según su ID.
Eliminar una tarea: Borra una tarea específica de la base de datos.
Diseñar el menú principal:

Presenta las opciones al usuario (CRUD + Salir).
Llama a las funciones correspondientes según la elección del usuario.
Maneja errores, como ingresar un ID inválido o seleccionar una opción incorrecta.
Probar el programa:

Inserta tareas de prueba para asegurarte de que el CRUD funcione correctamente.
Asegúrate de manejar excepciones, como errores de conexión a la base de datos o valores no válidos ingresados por el usuario.
Notas Adicionales
Utiliza condicionales, ciclos, y manejo de excepciones para validar entradas y asegurar el correcto funcionamiento del programa.
El programa debe ser modular, con cada funcionalidad implementada como una función independiente o método dentro de una clase.
Al finalizar, permite al usuario guardar su progreso y reanudar el trabajo en futuras ejecuciones del programa. """

import sqlite3  # Módulo para trabajar con bases de datos SQLite
from datetime import datetime  # Para manejar fechas


# Clase Tarea para representar una tarea
class Tarea:
    def __init__(self, id_tarea, descripcion, estado, fecha_limite):
        """
        Constructor para inicializar un objeto Tarea.
        :param id_tarea: Identificador único de la tarea (ID).
        :param descripcion: Descripción de la tarea.
        :param estado: Estado de la tarea ("Pendiente" o "Completada").
        :param fecha_limite: Fecha límite de la tarea (puede ser None).
        """
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_limite = fecha_limite

    def __str__(self):
        """
        Representación en cadena de una tarea.
        """
        fecha = self.fecha_limite if self.fecha_limite else "Sin fecha límite"
        return f"ID: {self.id_tarea} | Descripción: {self.descripcion} | Estado: {self.estado} | Fecha límite: {fecha}"


# Función para inicializar la base de datos
def inicializar_base_de_datos():
    """
    Crea la base de datos y la tabla de tareas si no existen.
    """
    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()  # Crear cursor para ejecutar comandos SQL
    # Crear la tabla "tareas" si no existe
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autoincremental
            descripcion TEXT NOT NULL,             -- Descripción de la tarea
            estado TEXT NOT NULL,                  -- Estado de la tarea
            fecha_limite TEXT                      -- Fecha límite (puede ser NULL)
        )
    """
    )
    conexion.commit()  # Confirmar cambios
    conexion.close()  # Cerrar conexión


# CRUD: Función para crear una tarea
def crear_tarea():
    """
    Solicita al usuario los datos de una tarea y la guarda en la base de datos.
    """
    descripcion = input("Ingresa la descripción de la tarea: ")
    estado = "Pendiente"  # Las nuevas tareas inician como "Pendiente"
    fecha_limite = input(
        "Ingresa la fecha límite (YYYY-MM-DD) o presiona Enter para omitir: "
    )
    fecha_limite = (
        fecha_limite if fecha_limite else None
    )  # Validar si se ingresó una fecha

    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()
    # Insertar la tarea en la tabla
    cursor.execute(
        "INSERT INTO tareas (descripcion, estado, fecha_limite) VALUES (?, ?, ?)",
        (descripcion, estado, fecha_limite),
    )
    conexion.commit()  # Confirmar cambios
    conexion.close()  # Cerrar conexión
    print("¡Tarea creada exitosamente!")


# CRUD: Función para leer todas las tareas
def leer_tareas():
    """
    Lee todas las tareas de la base de datos y las muestra.
    """
    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()
    # Consultar todas las tareas
    cursor.execute("SELECT id, descripcion, estado, fecha_limite FROM tareas")
    registros = cursor.fetchall()  # Obtener resultados
    conexion.close()  # Cerrar conexión

    if not registros:  # Validar si no hay registros
        print("No hay tareas registradas.")
    else:
        print("\nLista de tareas:")
        # Convertir cada registro en un objeto Tarea y mostrarlo
        for registro in registros:
            tarea = Tarea(*registro)  # Crear objeto Tarea con los datos
            print(tarea)


# CRUD: Función para actualizar una tarea
def actualizar_tarea():
    """
    Permite actualizar la descripción o la fecha límite de una tarea existente.
    """
    id_tarea = input("Ingresa el ID de la tarea a actualizar: ")
    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()
    # Consultar tarea por ID
    cursor.execute(
        "SELECT id, descripcion, estado, fecha_limite FROM tareas WHERE id = ?",
        (id_tarea,),
    )
    registro = cursor.fetchone()  # Obtener resultado

    if registro:  # Si existe la tarea
        tarea = Tarea(*registro)  # Crear objeto Tarea
        print(f"Tarea encontrada: {tarea}")
        # Solicitar nuevos datos
        nueva_descripcion = (
            input("Nueva descripción (déjalo vacío para no cambiar): ")
            or tarea.descripcion
        )
        nueva_fecha_limite = (
            input("Nueva fecha límite (YYYY-MM-DD, déjalo vacío para no cambiar): ")
            or tarea.fecha_limite
        )
        # Actualizar en la base de datos
        cursor.execute(
            """
            UPDATE tareas 
            SET descripcion = ?, fecha_limite = ? 
            WHERE id = ?
        """,
            (nueva_descripcion, nueva_fecha_limite, id_tarea),
        )
        conexion.commit()  # Confirmar cambios
        print("¡Tarea actualizada exitosamente!")
    else:
        print("Tarea no encontrada.")  # Si no existe la tarea

    conexion.close()  # Cerrar conexión


# CRUD: Función para cambiar el estado de una tarea
def cambiar_estado_tarea():
    """
    Marca una tarea como completada usando su ID.
    """
    id_tarea = input("Ingresa el ID de la tarea a marcar como completada: ")
    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()
    # Consultar tarea por ID
    cursor.execute(
        "SELECT id, descripcion, estado, fecha_limite FROM tareas WHERE id = ?",
        (id_tarea,),
    )
    registro = cursor.fetchone()  # Obtener resultado

    if registro:  # Si existe la tarea
        tarea = Tarea(*registro)  # Crear objeto Tarea
        print(f"Tarea encontrada: {tarea}")
        # Cambiar el estado a "Completada"
        cursor.execute(
            "UPDATE tareas SET estado = ? WHERE id = ?", ("Completada", id_tarea)
        )
        conexion.commit()  # Confirmar cambios
        print("¡Estado de la tarea actualizado a 'Completada'!")
    else:
        print("Tarea no encontrada.")  # Si no existe la tarea

    conexion.close()  # Cerrar conexión


# CRUD: Función para eliminar una tarea
def eliminar_tarea():
    """
    Elimina una tarea de la base de datos usando su ID.
    """
    id_tarea = input("Ingresa el ID de la tarea a eliminar: ")
    conexion = sqlite3.connect("tareas.db")  # Conexión a la base de datos
    cursor = conexion.cursor()
    # Consultar tarea por ID
    cursor.execute(
        "SELECT id, descripcion, estado, fecha_limite FROM tareas WHERE id = ?",
        (id_tarea,),
    )
    registro = cursor.fetchone()  # Obtener resultado

    if registro:  # Si existe la tarea
        tarea = Tarea(*registro)  # Crear objeto Tarea
        print(f"Tarea encontrada: {tarea}")
        confirmacion = input("¿Estás seguro de que deseas eliminar esta tarea? (s/n): ")
        if confirmacion.lower() == "s":
            cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
            conexion.commit()  # Confirmar cambios
            print("¡Tarea eliminada exitosamente!")
    else:
        print("Tarea no encontrada.")  # Si no existe la tarea

    conexion.close()  # Cerrar conexión


# Programa principal
def main():
    """
    Punto de entrada del programa.
    """
    inicializar_base_de_datos()  # Crear la base de datos si no existe
    while True:  # Ciclo principal
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Marcar tarea como completada")
        print("5. Eliminar tarea")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            leer_tareas()
        elif opcion == "3":
            actualizar_tarea()
        elif opcion == "4":
            cambiar_estado_tarea()
        elif opcion == "5":
            eliminar_tarea()
        elif opcion == "6":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


# Ejecutar el programa

main()

"""
Para crear un ejecutable instalamos la libreria pyinstaller
pip install pyinstaller 
y ejecutamos el comando dentro de la carpeta de nuestro archivo .py
pyinstaller --onefile archivo.py
"""
