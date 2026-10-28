#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio+
list=[]
counter=0
listlong=4
listsum=0
print(f"Ingrese {listlong} numeros")
for number in range(listlong):
    number= int(input(f"Ingrese su numero {counter+1}: "))
    listsum=listsum+number
    list.append(number)
avg=listsum/listlong
list2=[]
for number in (list):
    if number > avg:
        list2.append(number)
print(list2)