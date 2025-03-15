class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        """ Constructor de la clase Libro. """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        """ Cambia 'disponible' a False si el libro está disponible. """
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito.")
        else:
            print("El libro ya está prestado.")

    def devolver(self):
        """ Cambia 'disponible' a True si el libro estaba prestado. """
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto con éxito.")
        else:
            print("El libro ya estaba disponible.")

    def buscar(self, isbn_buscar):
        """ Devuelve el libro si el ISBN coincide, None en caso contrario. """
        return self if self.isbn == isbn_buscar else None

    def to_dict(self):
        """ Convierte el objeto Libro a un diccionario. """
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "disponible": self.disponible
        }

    @staticmethod
    def from_dict(data):
        """ Crea un objeto Libro a partir de un diccionario. """
        return Libro(data["titulo"], data["autor"], data["isbn"], data["disponible"])

    def __str__(self):
        """ Devuelve la información del libro en formato de texto. """
        estado = "Sí" if self.disponible else "No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"


def cargar_libros():
    """ Carga los libros desde un archivo JSON. """
    return [
                {
                    "titulo": "El Quijote",
                    "autor": "Cervantes ",
                    "isbn": "12345",
                    "disponible": True
                },
                {
                    "titulo": "El cuento de la criada",
                    "autor": "Margaret Atwood",
                    "isbn": "67890",
                    "disponible": True
                },
                {
                    "titulo": "Fundaci\u00f3n",
                    "autor": "Isaac Asimov",
                    "isbn": "11223",
                    "disponible": True
                }
            ]


def mostrar_biblioteca(biblioteca):
    """ Muestra la información de todos los libros en la biblioteca. """
    if biblioteca:
        for libro in biblioteca:
            print(libro)
    else:
        print("La biblioteca está vacía.")


# Cargar libros al iniciar
biblioteca = cargar_libros()

# Bucle principal del programa.
while True:
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        titulo_nuevo = input("Título: ")
        autor_nuevo = input("Autor: ")
        isbn_nuevo = input("ISBN: ")
        nuevo_libro = Libro(titulo_nuevo, autor_nuevo, isbn_nuevo)
        biblioteca.append(nuevo_libro)
        print("Libro agregado con éxito.")

    elif opcion == '2':
        isbn_prestar = input("Ingresa el ISBN del libro que deseas prestar: ")
        libro_encontrado = next((libro for libro in biblioteca if libro.buscar(isbn_prestar)), None)
        if libro_encontrado:
            libro_encontrado.prestar()
        else:
            print("No se encontró ningún libro con ese ISBN.")

    elif opcion == '3':
        isbn_devolver = input("Ingresa el ISBN del libro que deseas devolver: ")
        libro_encontrado = next((libro for libro in biblioteca if libro.buscar(isbn_devolver)), None)
        if libro_encontrado:
            libro_encontrado.devolver()
        else:
            print("No se encontró ningún libro con ese ISBN.")

    elif opcion == '4':
        mostrar_biblioteca(biblioteca)

    elif opcion == '5':
        isbn_buscar = input("Ingresa el ISBN del libro que deseas buscar: ")
        libro_encontrado = next((libro for libro in biblioteca if libro.buscar(isbn_buscar)), None)
        if libro_encontrado:
            print(libro_encontrado)
        else:
            print("No se encontró ningún libro con ese ISBN.")

    elif opcion == '6':
        print("¡Gracias por usar el sistema!")
        break

    else:
        print("Opción inválida. Por favor, elige una opción del menú.")
