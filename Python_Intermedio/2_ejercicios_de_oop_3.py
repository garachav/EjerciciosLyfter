# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario

class Product():
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity


class Inventory():
    def __init__(self):
        self.inventory_list=[]
    
    
    def add_product(self, product):
        self.inventory_list.append(product)


    def show_products(self):
        for product in self.inventory_list:
            print(f"El producto {product.name}, tiene un precio de {product.price}, se cuentan con {product.quantity} unidades")


    def calculate_total_value_of_inventory(self):
        total=0
        for product in self.inventory_list:
            total=total+product.price*product.quantity
        return total

product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
print(len(inventory.inventory_list))   # tiene que dar 2
inventory.show_products()
print(inventory.calculate_total_value_of_inventory())