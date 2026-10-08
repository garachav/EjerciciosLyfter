# Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
my_list=[]
counter=1
while counter!=6:
    word= input(str(f"Ingrese su palabra {counter}: "))
    counter=counter+1
    if len(word)>4:
        my_list.append(word)
print(my_list)