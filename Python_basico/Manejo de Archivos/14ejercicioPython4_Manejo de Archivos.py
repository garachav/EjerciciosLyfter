# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente

def text():
    text=str(input("Ingrese el texto: "))
    return text


def main(path1,):
    with open(path1, 'a', encoding='utf-8') as file:
        user_text= text()
        file.write(user_text+'\n')
            
            
main('notas.txt')