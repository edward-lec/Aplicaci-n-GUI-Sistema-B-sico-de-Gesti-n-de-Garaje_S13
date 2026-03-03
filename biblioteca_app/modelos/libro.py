# modelos/libro.py

class Libro:
    """
    Clase que representa la entidad Libro.

    Decisión de diseño:
    - Título y autor se almacenan en una TUPLA para garantizar inmutabilidad,
      ya que estos datos no deberían modificarse después de crear el libro.
    - Se aplica encapsulamiento usando atributos privados (__).
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable (requisito obligatorio)
        self.__info = (titulo, autor)

        # Otros atributos del libro
        self.__categoria = categoria
        self.__isbn = isbn

    # GETTERS
    # Se exponen solo métodos de lectura para proteger los datos

    def get_titulo(self):
        return self.__info[0]

    def get_autor(self):
        return self.__info[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    # Representación en texto del objeto
    def __str__(self):
        return (
            f"Título: {self.get_titulo()} | "
            f"Autor: {self.get_autor()} | "
            f"Categoría: {self.__categoria} | "
            f"ISBN: {self.__isbn}"
        )