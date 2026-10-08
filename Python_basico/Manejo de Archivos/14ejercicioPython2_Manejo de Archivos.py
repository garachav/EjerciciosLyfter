# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)

def words_counter(path1):
    with open(path1, 'r', encoding='utf-8') as file:
        songs = file.read()
        songs=songs.split()
        counter= len(songs)
        print(songs)
        print (f"Este archivo contiene {counter} palabras")


words_counter('songs.txt',)


