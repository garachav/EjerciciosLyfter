#Experimente con el concepto de scope:
#Intente acceder a una variable definida dentro de una función desde afuera.

def mi_funcion():
    variable_local = 10

mi_funcion()
print(variable_local)  
#da error


#Intente acceder a una variable global desde una función y cambiar su valor.

contador = 0

def mi_funcion():
    contador = 5  

mi_funcion()
print(contador)  
#tiene valor 0, no se altero