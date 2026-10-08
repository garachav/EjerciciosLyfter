your_number=(int(input("Adivine que número estoy pensando: ")))
import random
my_number= random.randint(1,10)
while your_number != my_number:
    your_number=(int(input("Su numero es incorrecto, intenta otra vez: ")))
print("Correcto!!!")
