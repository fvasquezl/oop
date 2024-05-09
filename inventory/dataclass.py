"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from dataclasses import field, dataclass

from functools import reduce
from itertools import count
from typing import List

id_gen = count(start=1, step=1).__next__


def float_validator(name, value, default=0.0, max_attempts=3):
    attempts = 0

    while attempts < max_attempts:
        if not value and default != 0.0:
            print(f"The value of {name} will be {default}")
            return default
        try:
            return float(value)
        except ValueError:
            attempts += 1
            print(f"Values for {name!r}  have to be a valid Number")
            value = input(f"{name}: ")
    print(
        f'The number of attempts({max_attempts}) has been exceeded the "{name}" value will be {default}'
    )

    return default


@dataclass
class Product:
    name: str = field(default="")
    price: float = field(repr=False, default=0.0)
    stock: float = field(repr=False, default=0.0)
    id: int = field(init=False, default_factory=id_gen)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}, {self.price}, {self.stock}"

    @classmethod
    def create_product(cls):
        name = input("Name: ")
        price = float_validator(name="Price", value=input("Price: "))
        stock = float_validator(name="Stock", value=input("Stock: "))
        return cls(name, price, stock)

    @classmethod
    def update_product(cls, product: "Product"):
        product.name = input("Name: ") or product.name
        product.price = float_validator(
            name="Price", value=input("Price: "), default=product.price
        )
        product.stock = float_validator(
            name="Stock", value=input("Stock: "), default=product.stock
        )
        return product


@dataclass
class Inventory:
    products: List[Product] = field(default_factory=list)

    def create_product(self):
        new_product = Product.create_product()
        self.products.append(new_product)
        print(f"The new product has been created")

    def read_products(self):
        if not self.products:
            print("There are no products for the list")
        for product in self.products:
            print(product)

    def update_product(self):
        while True:
            try:
                id = int(input("Id, of the product to update: "))
                product = [x for x in self.products if x.id == id][0]
                break
            except:
                print("The Id does not exist")

        Product.update_product(product)
        print(f"The product has been updated")

    def delete_product(self):
        while True:
            try:
                id = int(input("Id Product for remove: "))
                product = [x for x in self.products if x.id == id][0]
                break
            except:
                print("The Id does not exist")

        self.products.remove(product)
        print(f"The product has been removed")

    def total_stock(self):
        total_stock = reduce((lambda x, y: x + y), [x.stock for x in self.products])
        print(f"Total Stock: {total_stock}")
        return total_stock


@dataclass
class Main:
    def menu(cls):
        inventory = Inventory()
        while True:
            print("\n     Menu ")
            print("1. Create product")
            print("2. Read products")
            print("3. Update product")
            print("4. Delete product")
            print("5. Inventory Total")
            print("6. Salir")
            choice = int(input("Option: "))

            if choice == 1:
                inventory.create_product()
            elif choice == 2:
                inventory.read_products()
            elif choice == 3:
                inventory.read_products()
                inventory.update_product()
            elif choice == 4:
                inventory.read_products()
                inventory.delete_product()
            elif choice == 5:
                inventory.total_stock()
            elif choice == 6:
                break
            else:
                print("Wrong Option")


if __name__ == "__main__":
    main = Main()
    main.menu()
