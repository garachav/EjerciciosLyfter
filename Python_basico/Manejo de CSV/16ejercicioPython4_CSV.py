# Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

import csv

def video_games_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader)
        developers={}
        for video_game in reader:
            name= video_game[0]
            genre= video_game[1]            
            developer= video_game[2]
            esrb_rating=video_game[3]
            if developer in developers:
                developers[developer].append({"Nombre": name, "Clasificacion": esrb_rating, "Genero": genre})
            else:
                developers[developer]=[{"Nombre":name,"Clasificacion":esrb_rating,"Genero":genre }]
        return developers


def format(file_path):
    while True:
        try:
            developer_inq= str(input(f"Cual desarrollador desea revisar?: "))
            the_developers_dictionary=video_games_list(file_path)
            print(f"Videojuegos desarrollados por: {developer_inq}")
            for video_game in the_developers_dictionary[developer_inq]:
                name= video_game['Nombre']
                genre=video_game['Genero']             
                esrb_rating=video_game['Clasificacion']
                print(f"- {name} (Clasificación: {esrb_rating}, Género: {genre})")
            break
        except KeyError:
            print(f"Desarrollador invalido, intente de nuevo")  


if __name__ == '__main__':
    format('Video_Games.csv')