# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:

import json


def main(file_path):
    pokemon_types=type_list(file_path)
    with open(file_path,"r",encoding='utf-8') as file:
        pokemons = json.load(file)
        for pokemon_type in pokemon_types:
            power_sum=0
            counter=0
            for pokemon in pokemons:
                if pokemon['type']== pokemon_type:
                    power_sum=pokemon['level']+power_sum
                    counter=counter+1
            print(f"Tipo: {pokemon_type} → Promedio de nivel: {power_sum/counter}")


def type_list(file_path):
    pokemon_types=[]
    with open(file_path,"r",encoding='utf-8') as file:
        pokemons = json.load(file)
        for pokemon in pokemons:
            if pokemon['type'] not in pokemon_types:
                pokemon_types.append(pokemon['type'])
        return pokemon_types


if __name__ == '__main__':
    main('pokemones.json')