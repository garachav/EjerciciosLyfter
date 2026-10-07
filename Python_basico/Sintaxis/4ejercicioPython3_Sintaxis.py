your_number= int(input ("Ingrese su numero:"))
addend=0
counter=0
while counter != your_number:
    counter=counter+1
    addend=counter+addend
print(f"El resultado final es {addend}")