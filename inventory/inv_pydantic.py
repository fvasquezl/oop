"""
**Implementa un sistema de gestión de inventario**
- Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
- Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
- Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

from decimal import Decimal
from typing import Annotated
import uuid
from pydantic import BaseModel, Field, computed_field
from pydantic.dataclasses import dataclass


PositiveInt = Annotated[int, Field(gt=0)]


@dataclass
class Product(BaseModel):
    name: str = Field(min_length=2)
    price: Decimal = Field(max_digits=5, decimal_places=2)
    id: uuid.UUID


foo = Product(name="faustino", price=Decimal("123.45"))

print(foo)
