# modelos/usuario.py

class Usuario:
    """
    Clase que representa la entidad Usuario.

    Decisión de diseño:
    - Se utiliza una LISTA para almacenar libros prestados (requisito obligatorio).
    - La lista permite agregar y eliminar libros dinámicamente.
    - Se aplica encapsulamiento para proteger los datos internos.
    """

    def __init__(self, nombre, user_id):
        self.__nombre = nombre
        self.__user_id = user_id

        # Lista obligatoria para libros prestados
        self.__libros_prestados = []

    # GETTERS

    def get_nombre(self):
        return self.__nombre

    def get_user_id(self):
        return self.__user_id

    def get_libros_prestados(self):
        return self.__libros_prestados

    # MÉTODOS DE NEGOCIO

    def agregar_libro(self, libro):
        """
        Añade un libro a la lista de préstamos del usuario.
        """
        self.__libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        """
        Busca un libro por ISBN dentro de los prestados y lo elimina.
        Retorna el libro si lo encuentra.
        """
        for libro in self.__libros_prestados:
            if libro.get_isbn() == isbn:
                self.__libros_prestados.remove(libro)
                return libro
        return None