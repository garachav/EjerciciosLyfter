number1=int(input("Ingresa su primer numero: "))
number2=int(input("Ingresa su segundo numero: "))
number3=int(input("Ingresa su tercer numero: "))
highest_number=0
if(number1>number2):
    highest_number=number1
else:
    highest_number=number2
if(number3>highest_number):
    highest_number= number3
print(f"Su numero mas alto es el {highest_number}")