#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

str="python-variable-funcion-computadora-monitor"
def order(str):
    list_str=str.split("-")
    list_str.sort()
    new_str= "-".join(list_str)
    print(new_str)
order(str)