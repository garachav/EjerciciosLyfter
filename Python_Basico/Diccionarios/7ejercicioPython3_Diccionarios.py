#Cree un programa que use una lista para eliminar keys de un diccionario
#Ejemplos:
#→ {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 
            'email': 'john@ecorp.com', 
            'access_level': 5, 
            'age': 28}
for i in range(len(list_of_keys)):
    deleted_item = employee.pop(list_of_keys[i])
print(employee)

