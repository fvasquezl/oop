"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel, Field


PositiveInt = Annotated[int, Field(gt=0)]


class Product(BaseModel):
    name: str = Field(max_digits=2)
    price: Decimal = Field(max_digits=5, decimal_places=2)
    # id: PositiveInt


foo = Product(name="faustino", price=Decimal("123.45"))

print(foo)
