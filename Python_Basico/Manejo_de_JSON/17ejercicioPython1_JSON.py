# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def main(file_path):
    
    pokemon=add_pokemon()
    file_exist=[]
    with open(file_path,"r",encoding='utf-8') as file:
        file_exist = json.load(file)
    file_exist.append(pokemon)
    with open(file_path,"w",encoding='utf-8') as file:
        json.dump(file_exist,file)


def add_pokemon():
    while True:
        try:
            pokemon_name= str(input(f"Cual es el nombre del Pokemon?: "))
            pokemon_type= str(input(f"Cual es el tipo del Pokemon?: "))
            pokemon_level= int(input(f"Cual es el nivel del Pokemon?: "))
            pokemon={'name':pokemon_name,'type':pokemon_type,'level':pokemon_level}
            return pokemon
        except ValueError:
            print(f"Informacion invalida, intente de nuevo")  


if __name__ == '__main__':
    main('pokemones.json')