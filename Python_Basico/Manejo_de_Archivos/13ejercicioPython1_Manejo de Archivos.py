# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
# Lea sobre el resto de métodos de la clase File de Python aquí y cree una tabla donde explique qué hace cada uno. 


def read_songs(path1):
    with open(path1, 'r', encoding='utf-8') as file:
        songs = file.readlines()
        songs.sort()
        print (type(songs))
        print (songs)
        return songs


def write_songs(path1,path2):
    with open(path2, 'w', encoding='utf-8') as file:
        for song in read_songs(path1):
            file.write(song)

write_songs('songs.txt','songs_sort.txt')


import os
print(f"your cd es{os.getcwd()}")