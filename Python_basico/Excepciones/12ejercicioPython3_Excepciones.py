# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total


def my_list():
    the_list=[]
    word=""
    counter=0
    while counter < 5:
        word= input(f"Ingrese su palabra {counter+1}: ")
        counter=counter+1
        the_list.append(word)
    return the_list

# def my_list():
#     the_list = ['10', 'manzana', '5.5', '3', 'n/a']
#     return the_list



def converter_float():
    the_list=my_list()
    sum=0
    print("Resultado: ")
    for item in the_list:
        try:
            old_item=item
            if"'" in item:
                item=item.replace("'","")
                sum=sum+float(item)
                print(f"{old_item} sumado correctamente")
            elif '"' in item:
                item=item.replace('"','')
                sum=sum+float(item)
                print(f"{old_item} sumado correctamente")
            else:
                sum=sum+float(item)
            print(f"{old_item} sumado correctamente")
        except ValueError:
                print(f"Elemento invalido: {old_item}")    
    print(f"Total de la suma: {sum}")

if __name__ == '__main__':
    converter_float()





# def converter_float():
#     the_list=my_list()
#     sum=0
#     print("Resultado: ")
#     for item in the_list:
#         if"'" in item:
#             old_item=item
#             item=item.replace("'","")
#             try:
#                 sum=sum+float(item)
#                 print(f"{old_item} sumado correctamente")
#             except ValueError:
#                 print(f"Elemento invalido: {old_item}")            
#         elif '"' in item:
#             old_item=item
#             item=item.replace('"','')
#             try:
#                 sum=sum+float(item)
#                 print(f"{old_item} sumado correctamente")
#             except ValueError:
#                 print(f"Elemento invalido: {old_item}")
#         else:
#             old_item=item
#             try:
#                 sum=sum+float(item)
#                 print(f"{old_item} sumado correctamente")
#             except ValueError:
#                 print(f"Elemento invalido: {old_item}")
#     print(f"Total de la suma: {sum}")


