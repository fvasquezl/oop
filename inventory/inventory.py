"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from dataclasses import asdict, field, dataclass

from itertools import count
from typing import Annotated, List

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

    @classmethod
    def add_products(cls, c_inv) -> Product:
        product = cls.create_product()
        c_inv.products.append(product)
        return product

    @classmethod
    def list_products(cls, c_inv) -> List[Product]:
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

    def remove_products():
        pass

    def update_products():
        pass

    def total_inventory():
        pass


if __name__ == "__main__":

    p1 = Product("product1", 16, 30)
    p2 = Product("product2", 15, 109)
    p3 = Product("product3", 14, 50)
    inv = Inventory(products=[p1, p2, p3])
    # inv.add_products(inv)
    inv.list_products(inv)
