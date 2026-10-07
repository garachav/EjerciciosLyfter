# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo


def read_file(path1):
    with open(path1, 'r', encoding='utf-8') as file:
        words = file.readlines()
        wordscap=[]
        for word in words:
            word=word.upper()
            wordscap.append(word)
            print (word)
        return wordscap


def write_fileCAP(path1,path2):
    with open(path2, 'w', encoding='utf-8') as file:
        for word in read_file(path1):
            file.write(word)


write_fileCAP('Hola mundo.txt','Hola mundoCAP.txt')