# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
#   Nombre
#   Género
#   Desarrollador
#   Clasificación ESRB

import csv

def save_video_games_list(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
def collect_videogames():
    video_games=[]
    counter=1
    n=int(input(f"Cuantos videojuegos desea agregar?: "))
    for vg in range (n):
        video_game={}
        name= str(input(f"Ingrese el nombre de su videojuego numero {counter}: "))
        video_game['Name']=name
        genre= str(input(f"Ingrese el genero de su videojuego numero {counter}: "))
        video_game['Genre']=genre
        developer= str(input(f"Ingrese el desarrollador de su videojuego numero {counter}: "))
        video_game['Developer']=developer
        esrb_rating= str(input(f"Ingrese clasificacion de su videojuego numero {counter}: "))
        video_game['ESRB Rating']=esrb_rating
        video_games.append(video_game)
        counter=counter+1
    return video_games






save_video_games_list('Video_Games.csv', collect_videogames())