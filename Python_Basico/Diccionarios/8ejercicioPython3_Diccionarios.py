#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},]

by_category = {}
for product in products:
    category = product['category']
    price = product['price']
    if category in by_category:
        by_category[category]=by_category[category]+price
    else:
        by_category[category]=price
print(by_category)



