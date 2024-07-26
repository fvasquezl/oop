"""
3. **Implementa un sistema de gestión de una biblioteca**
   - Crea una clase `Libro` con atributos como título, autor, año de publicación y cantidad disponible.
   - Crea una clase `Miembro` para representar a los miembros de la biblioteca, con información como nombre, dirección y libros prestados.
   - Implementa una clase `Biblioteca` que gestione una lista de libros y miembros, permitiendo prestar y devolver libros, así como ver los libros disponibles y los miembros con libros prestados.
"""

from dataclasses import dataclass, field
from typing import List
import os

from myclass.book import Book
from myclass.member import Member


@dataclass
class Library:
    books: List[Book] = field(default_factory=list)
    members: List[Member] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"All Books: {self.books}\n" f"All Memebers:{self.members}\n"

    def menu(self):
        return {
            1: "Agregar Libros",
            2: "Listar Libros",
            3: "Agregar Usuarios",
            4: "Prestar Libro",
            5: "Devolver Libro",
            6: "Libros disponibles",
            7: "Usuarios con Libros prestados",
            "x": "Salir",
        }

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def menu_title(self, character="-", qty=5, title="Title"):
        line = character * qty
        print(f"{line} {title} {line}")

    def display_menu(self):
        options = self.menu()
        self.menu_title("*", 12, "Menu Principal")
        for key, value in options.items():
            print(f"[{key}] {value}")
        print("-" * 40)

    def get_user_option(self):
        while True:
            option = input("Selecciona una opcion: ").strip().upper()
            if option == "X":
                print("Saliendo del programa")
                exit()
            try:
                option = int(option)
                if option not in self.menu():
                    print("Opcion fuera de rango. Intente de nuevo")
                else:
                    return option
            except ValueError:
                print("Entrada Invalida. Ingrese un numero 'x' para salir")

    def run_menu(self):
        while True:
            self.clear_screen()
            self.display_menu()
            user_option = self.get_user_option()

            if user_option == 1:
                self.addBook()

            if user_option == 2:
                self.listBooks()

    def addBook(self):
        self.menu_title("-", 10, "Agregar Libro")
        title = input("Titulo: ")
        author = input("Autor: ")
        while True:
            try:
                year = int(input("Año de publicacion: "))
                book = Book(title=title, author=author)
                book.year = year
                break
            except ValueError:
                print("Entada invalida. Ingrese un año valido (1492 a la fecha)")

        while True:
            try:
                qty = int(input("Cantidad: "))
                book.qty = qty
                break
            except ValueError:
                print("Entrada invalida. Ingrese una cantidad valida")

        self.books.append(book)
        print(f"Libro '{title}' por {author} agregado correctamente")

    def listBooks(self):
        for book in self.books:
            print(book)

        input("Press Key to continue")


if __name__ == "__main__":
    library = Library()
    library.run_menu()
