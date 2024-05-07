"""
1. **Implementa un sistema de gestión de inventario**
   - Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock.
   - Crea una clase `Inventario` que contenga una lista de productos y métodos para agregar, eliminar y actualizar productos, así como para calcular el valor total del inventario.
   - Implementa un menú interactivo para que el usuario pueda interactuar con el sistema de gestión de inventario.
"""

import itertools


class Product:
    new_id = itertools.count()

    def __init__(self, name, price, stock):
        self.id = next(self.new_id)
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = []

    def list_product(self):
        print("\n--Listing Products--")
        if not len(self.products):
            print("No hay productos")
            return
        for product in self.products:
            print(product)
        return

    def find_product(self, msg):
        self.list_product()
        while True:
            option = int(input(f"{msg}: "))
            product = [x for x in self.products if x.id == option]
            if len(product) == 1:
                return product[0]
            print("Selecciona el ID de un producto")

    def remove_product(self):
        print("\n--Product Remove--")
        product = self.find_product("Producto a eliminar")
        self.products.remove(product)

    def update_product(self):
        print("\n--Update Remove--")
        product = self.find_product("Producto a Actualizar")
        product.name = input("Name:") or product.name
        product.price = input("Price:") or product.price
        product.stock = input("Stock:") or product.stock
        print(product)

    def add_product(self):
        print("\n--Add Product--")
        name = input("Name:")
        price = input("Price:")
        stock = input("Stock:")
        self.products.append(Product(name, price, stock))
        return

    def total_stock(self):
        print("\n--Total Stock--")
        total = sum([int(x.stock) for x in self.products])
        print(f"TotalStock: {total}")
        return

    def menu_inventory(self):
        while True:
            print("\n     Menu ")
            print("1. Listar productos")
            print("2. Agregar producto")
            print("3. Eliminar producto")
            print("4. Actualizar producto")
            print("5. Total del inventario")
            print("6. Salir")
            choice = int(input("Opcion: "))

            if choice == 1:
                self.list_product()
            elif choice == 2:
                self.add_product()
            elif choice == 3:
                self.remove_product()
            elif choice == 4:
                self.update_product()
            elif choice == 5:
                self.total_stock()
            elif choice == 6:
                break
            else:
                print("Opcion Incorrecta")
        return


if __name__ == "__main__":
    inventory = Inventory()
    inventory.menu_inventory()
