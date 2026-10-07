#Cree un programa que elimine todos los números impares de una lista.
my_list = [1, 2, 2, 4, 5, 5, 7, 8, 9,10,11,12]

my_list2 = []
for number2 in my_list:
    if (number2%2 == 0):
        my_list2.append(number2)
print(my_list2)


#Codigo malo:
#for number in my_list:
#    if (number%2 != 0):
#        my_list.remove(number)
#print(my_list)