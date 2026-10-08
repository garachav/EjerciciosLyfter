# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json


def main(file_path):
    for pokemon in pokemon_list(file_path):
        print(f"Nombre: {pokemon['name']}")    
        print(f"Ataque: {pokemon['stats']['attack']}")
        print(f"Defensa: {pokemon['stats']['defense']}")
        print(f"Velocidad: {pokemon['stats']['speed']}\n")

def pokemon_list(file_path):
    with open(file_path,"r",encoding='utf-8') as file:
        pokemons = json.load(file)
        return pokemons


def pokemon_type():
    user_pokemon_type= str(input(f"Ingrese el tipo de pokemon desea buscar(water, electric, fire,etc): "))
    return user_pokemon_type


if __name__ == '__main__':
    main('pokemones.json')