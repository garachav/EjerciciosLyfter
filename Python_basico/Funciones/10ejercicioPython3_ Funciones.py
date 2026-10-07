#Cree una función que reciba un string y retorne cuántas vocales contiene

def searcher(text,vowels):
    counter=0
    for letter in text:
        if letter in vowels:
            counter=counter+1
    print(f"Se han encontrado {counter} vocales")

text=input(f"Ingrese el texto donde desea buscar: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]


searcher(text,vowels)
