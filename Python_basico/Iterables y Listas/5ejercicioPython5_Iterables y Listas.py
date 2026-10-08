#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.+
my_list=[]
highest= int(input("Ingrese su numero: "))
my_list.append (highest)
for number in range(9):
    number= int(input("Ingrese su numero: "))
    if number>highest:
        highest=number
    my_list.append (number)
print(my_list," El más alto fue ",highest)