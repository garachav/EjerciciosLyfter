number1=int(input("Ingresa su primer numero: "))
number2=int(input("Ingresa su segundo numero: "))
number3=int(input("Ingresa su tercer numero: "))
if number1==30 or number2==30 or number3==30:
    print ("Correcto")
elif number1+number2+number3==30:
    print ("Correcto")
else:
    print ("Incorrecto")