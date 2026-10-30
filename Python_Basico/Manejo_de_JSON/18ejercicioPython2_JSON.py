# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo

import json


def main(file_path):
    user_pokemon_type=pokemon_type()
    user_pokemons=[]
    with open(file_path,"r",encoding='utf-8') as file:
        pokemons = json.load(file)
        for pokemon in pokemons:
            if user_pokemon_type.upper()== pokemon['type'].upper():
                user_pokemons.append(pokemon['name'])
    print(f"Los pokemones que existen de ese tipo son: {user_pokemons}")


def pokemon_type():
    user_pokemon_type= str(input(f"Ingrese el tipo de pokemon desea buscar(water, electric, fire,etc): "))
    return user_pokemon_type


if __name__ == '__main__':
    main('pokemones.json')