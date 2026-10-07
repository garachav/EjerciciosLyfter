number= int(input("Ingrese su numero del 1 al 12: "))
while number<1 or number>12:
    number=int(input("Pongase serio, digite un numero del 1 al 12: "))
counter=1
while counter!=13:
    print(f"{number} X {counter} = {number*counter}")
    counter=counter+1