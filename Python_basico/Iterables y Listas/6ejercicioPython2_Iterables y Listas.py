#Cree un programa que verifique si todos los elementos de una lista son positivos
list=[54, 35, 56, 4]
positive_numbers=0
negative_numbers=0
number0=0
for number in list:
    if number >0:
        positive_numbers=positive_numbers+1
    elif number<0:
        negative_numbers= negative_numbers+1
    else:
        number0=number0+1
if number0 >0 or negative_numbers>0:
    print("Hay al menos un número negativo o cero")
else:
    print("Solo hay numeros positivos")