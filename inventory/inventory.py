"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from dataclasses import asdict, field, dataclass
from itertools import count
from typing import List
from tabulate import tabulate

id_gen = count(start=100, step=1).__next__


@dataclass
class Product:
    id: int = field(default_factory=id_gen, init=False)
    name: str = field(default="")
    price: float = field(repr=False, default=0.0)
    stock: float = field(repr=False, default=0.0)

    def __repr__(self) -> str:
        return (
            f"Id: {self.id}"
            f"\nName: {self.name}"
            f"\nPrice {self.price}"
            f"\nStock {self.stock}"
        )


@dataclass
class Inventory:
    products: List[Product] = field(default_factory=list)

    @staticmethod
    def create_product() -> Product:
        name = input("Name: ")
        price = float(input("Price: "))
        stock = float(input("Stock: "))
        product = Product(name=name, price=price, stock=stock)
        return product

    @staticmethod
    def update_product(product) -> Product:
        name = input(f"Name ({product.name}): ")
        if name:
            product.name = name
        price = input(f"Price ({product.price}): ")
        if price:
            product.price = float(price)
        stock = input(f"Stock ({product.stock}): ")
        if stock:
            product.stock = float(stock)
        return product

    @classmethod
    def list_products(cls, c_inv) -> None:
        headers = []
        data = []
        total_stock = 0
        if c_inv.products:
            headers = list(asdict(c_inv.products[0]).keys())
        for product in c_inv.products:
            total_stock += product.stock
            data.append(list(asdict(product).values()))
        print(tabulate(data, headers=headers))
        print("_____________")
        print(f"Total Stock: {total_stock}")

    @classmethod
    def create_products(cls, c_inv) -> None:
        try:
            product = cls.create_product()
            c_inv.products.append(product)
        except ValueError:
            print("El valor ingresado es incorrecto")

    @classmethod
    def update_products(cls, c_inv) -> None:
        try:
            id = int(input("Producto a actualizar: "))
            product = next((x for x in c_inv.products if x.id == id), None)
            if product:
                cls.update_product(product)
                print(f"El producto {id} ha sido actualizado")
            else:
                print("El productos seleccionado no existe")
        except ValueError:
            print("El valor ingresado es incorrecto")

    @classmethod
    def remove_products(cls, c_inv) -> None:
        try:
            id = int(input("Producto a eliminar: "))
            product = next((x for x in c_inv.products if x.id == id), None)
            if product:
                c_inv.products.remove(product)
                print(f"El producto {id} ha sido elimnado")
            else:
                print("El productos seleccionado no existe")
        except ValueError:
            print("El valor ingresado es incorrecto")


@dataclass
class Main:
    inventory = Inventory()  # Variable de clase

    @staticmethod
    def menu():
        options = {
            1: "Lista de productos",
            2: "Crear Productos",
            3: "Actualizar Productos",
            4: "Eliminar Productos",
            5: "Salir",
        }
        actions = {
            1: Main.inventory.list_products,
            2: Main.inventory.create_products,
            3: Main.inventory.update_products,
            4: Main.inventory.remove_products,
        }
        while True:
            print("\nMenu Principal:")
            for option, description in options.items():
                print(f"[{option}] {description}")
            try:
                choice = int(input("Opcion Seleccionada:"))
                if choice in options:
                    if choice == 5:
                        print("Hasta la vista Baby!")
                        break
                    else:
                        actions[choice](Main.inventory)
                else:
                    print("La opcion seleccionada es invalida")

            except ValueError as e:
                print("Please enter a valid number.")
            except Exception as e:
                print(repr(e))


if __name__ == "__main__":
    Main.menu()
