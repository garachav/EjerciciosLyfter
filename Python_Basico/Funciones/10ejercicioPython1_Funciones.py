#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

def searcher(text,look_up):
    counter=0
    for letter in text:
        if letter== look_up:
            counter=counter+1
    print(f"Se ha encontrado {counter} veces el carácter")

text=input(f"Ingrese el texto donde desea buscar:")
look_up=input(f"Ingrese el carácter que desea buscar:")


searcher(text,look_up)
