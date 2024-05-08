"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from dataclasses import field, dataclass

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
    id: int = field(default_factory=id_gen)

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

    def product_list(self):
        if not self.products:
            print("No hay productos para listar")
        for product in self.products:
            print(product)

    def create_product(self):
        new_product = Product.create_product()
        self.products.append(new_product)
        print(f"Nuevo producto creado: {new_product}")

    def product_update(self):
        self.product_list()
        try:
            id = int(input("Id, del producto a actualizar: "))
            product = [x for x in self.products if x.id == id]
            updated_product = Product.update_product(product[0])
        except IndexError:
            print("El numero ingresado esta fuera de rango")
        print(f"Producto actualizado")


@dataclass
class Main:

    inv = Inventory()
    inv.create_product()
    inv.product_update()
    inv.product_list()
