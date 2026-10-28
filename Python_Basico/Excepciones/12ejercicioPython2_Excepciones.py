# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás




def my_list():
    the_list=[]
    word=""
    counter=0
    while counter < 5:
        word= input(f"Ingrese su palabra {counter+1}: ")
        counter=counter+1
        the_list.append(word)
    return the_list


def converter_int():
    the_list=my_list()
    print("Resultado: ")
    for item in the_list:
        old_item=item
        try:
            if"'" in item:
                item=item.replace("'","")
                print(f"{old_item} convertido a {int(item)}")
            elif '"' in item:
                item=item.replace('"','')
                print(f"{old_item} convertido a {int(item)}")
            elif '.' in item:
                item=float(item)
                item=int(item)
                print(f"{old_item} convertido a {int(item)}")
            else:
                print(f"{item} convertido a {int(item)}")        
        except ValueError:
            print(f"No se pudo convertir el elemento: {old_item}")


if __name__ == '__main__':
    converter_int()



# def converter_int():
#     the_list=my_list()
#     print("Resultado: ")
#     for item in the_list:
#         if"'" in item:
#             old_item=item
#             item=item.replace("'","")
#             try:
#                 print(f"{old_item} convertido a {int(item)}")
#             except ValueError:
#                 print(f"No se pudo convertir el elemento: {old_item}")            
#         elif '"' in item:
#             old_item=item
#             item=item.replace('"','')
#             try:
#                 print(f"{old_item} convertido a {int(item)}")
#             except ValueError:
#                 print(f"No se pudo convertir el elemento: {old_item}")
#         elif '.' in item:
#             old_item=item
#             item=float(item)
#             item=int(item)
#             try:
#                 print(f"{old_item} convertido a {int(item)}")
#             except ValueError:
#                 print(f"No se pudo convertir el elemento: {old_item}")
#         else:
#             old_item=item
#             try:
#                 print(f"{item} convertido a {int(item)}")
#             except ValueError:
#                 print(f"No se pudo convertir el elemento: {old_item}")