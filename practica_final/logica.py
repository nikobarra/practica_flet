import sqlite3


# Configuración inicial de la base de datos
def init_db():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS favoritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            libro_id INTEGER NOT NULL,
            FOREIGN KEY(libro_id) REFERENCES libros(id)
        )
        """
    )
    conn.commit()
    conn.close()


# Función para cargar libros
def get_books():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor FROM libros")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Función para cargar favoritos
def get_favorites():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT libros.id, libros.titulo, libros.autor
        FROM favoritos
        JOIN libros ON favoritos.libro_id = libros.id
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# Función para añadir un libro
def add_book_to_db(title, author):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor) VALUES (?, ?)", (title, author))
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return book_id


# Función para eliminar un libro
def delete_book_from_db(book_id):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (book_id,))
    cursor.execute("DELETE FROM favoritos WHERE libro_id = ?", (book_id,))
    conn.commit()
    conn.close()


# Función para añadir un libro a favoritos
def add_to_favorites(book_id):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM favoritos WHERE libro_id = ?", (book_id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO favoritos (libro_id) VALUES (?)", (book_id,))
        conn.commit()
    conn.close()
