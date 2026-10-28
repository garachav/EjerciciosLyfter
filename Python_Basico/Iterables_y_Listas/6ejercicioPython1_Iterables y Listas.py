#Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
list=[]
counter=0
listlong=20
print(f"Ingrese {listlong} numeros")
for number in range(listlong):
    number= int(input(f"Ingrese su numero {counter+1}: "))
    list.append (number)
    counter=counter+1
search_number_counter=0
search_number=int(input("Cual numero buscamos?: "))
for number in list:
    if number == search_number:
        search_number_counter=search_number_counter+1
print(list)
print(f"El numero {search_number}, aparece {search_number_counter} ")
