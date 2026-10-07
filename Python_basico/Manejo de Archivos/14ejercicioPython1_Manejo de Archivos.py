#Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo


def read_words(path1):
    with open(path1, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        lines=" ".join(lines)
        print(lines)
        return lines



def write_words(path1,path2):
    with open(path2, 'w', encoding='utf-8') as file:
        file.write(read_words(path1))


write_words('Hola mundo.txt','Hola mundo en una linea.txt')

import os
print(f"your cd es{os.getcwd()}")