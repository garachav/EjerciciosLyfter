# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv

def user_esrb_rating(file_path):
    while True:
        try:
            esrb= str(input("Ingrese la clasificacion que desea buscar: ")).upper()
            find=False
            with open(file_path, 'r', encoding='utf-8') as file:
                reader=csv.reader(file)
                next(reader)
                for video_game in reader:
                    if esrb == video_game[3].upper():
                        find=True
                        return esrb
            if find==False:
                raise ValueError()
        except ValueError as e:
            print("Categoria invalida ")  



def video_games_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader)
        user_esrb= user_esrb_rating(file_path)
        for video_game in reader:
            name= video_game[0]
            genre= video_game[1]            
            developer= video_game[2]
            esrb_rating=video_game[3]
            if esrb_rating== user_esrb:
                print("Nombre:", name)
                print("Género:", genre)
                print("Desarrollador:", developer)
                print("Clasificación:", esrb_rating) 
                print("-" * 100)


if __name__ == '__main__':
    video_games_list('Video_Games.csv')