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


@dataclass
class Product:
    name: str
    price: float
    stock: float
    id: int = field(default_factory=id_gen)


@dataclass
class Inventory:
    products: List[Product] = field(default_factory=list)

    def product_list(self):
        for i in self.products:
            print(i)


@dataclass
class Main:
    p1 = Product("Producto A", 10.5, 20)
    p2 = Product("Producto B", 15.0, 30)
    p3 = Product("Producto C", 16.0, 80)
    inv = Inventory()
    inv.products.append(p1)
    inv.products.append(p2)
    inv.products.append(p3)
    inv.product_list()
