# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

import csv

def video_games_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader)
        genres={}
        for video_game in reader:
            genre=video_game[1]
            if genre in genres:
                genres[genre] = genres[genre] + 1
            else:
                genres[genre]=1
#        print(genres)
        return genres


def format(file_path):
    the_genre_dictionary=video_games_list(file_path)
    print("Géneros encontrados:")
    for genre, quantity in the_genre_dictionary.items():
        print(f'{genre}:{quantity}')


if __name__ == '__main__':
    format('Video_Games.csv')


