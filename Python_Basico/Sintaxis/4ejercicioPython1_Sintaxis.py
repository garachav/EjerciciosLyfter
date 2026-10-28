price=float(input("Digite el precio del producto: "))
while price<0:
    price=float(input("Precio incorrecto, digite el precio correcto: "))
if (price<100):
    discount=price*.02
else:
    discount=price*.1
print(f"El precio final es de {price-discount}")