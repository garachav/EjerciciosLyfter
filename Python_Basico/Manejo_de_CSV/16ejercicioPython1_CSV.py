# Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

import csv

def video_games_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader)
        for video_game in reader:
            print("Nombre:", video_game[0])
            print("Género:", video_game[1])
            print("Desarrollador:", video_game[2])
            print("Clasificación:", video_game[3])
            print("-" * 100)

if __name__ == '__main__':
    video_games_list('Video_Games.csv')