# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json

def main(file_path):
    for pokemon in pokemon_list(file_path):
        print(f"El nombre del pokemon es: {pokemon['name']}, el tipo es {pokemon['type']} y su nivel es {pokemon['level']}")


def pokemon_list(file_path):
    with open(file_path,"r",encoding='utf-8') as file:
        pokemons = json.load(file)
        return pokemons


if __name__ == '__main__':
    main('pokemones.json')