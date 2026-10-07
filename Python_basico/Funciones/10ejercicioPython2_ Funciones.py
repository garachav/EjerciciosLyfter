#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras


def filter (user_list,minim_letters):
    new_list=[]
    for word in user_list:
        if len(word)>= minim_letters:
            new_list.append(word)
    print(new_list)

counter=0
user_list=[]
while counter != 4:
    user_list.append(input("Ingrese la palabra que desea agregar a la lista: "))
    counter=counter+1

minim_letters=int(input("Ingrese el minimo de letras que debe de tener cada palabra: "))
filter (user_list,minim_letters)