#Cree un programa que muestre el valor más pequeño de una lista sin usar
list=[54, 58, 740, 5, 4584, 858, -4, 40, 454, 54, 45, 10, 630, 90, 54, 1, 90, 99, 4, 54]
min_number= list[0]
for number in list:
    if number<min_number:
        min_number=number
print(f"El menor valor es {min_number}")
