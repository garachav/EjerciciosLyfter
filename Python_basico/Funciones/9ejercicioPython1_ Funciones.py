#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_your_name():
    print (input("What is your name? "))
    print_your_lastname()


def print_your_lastname():
    print(input ("What is your lastname?: "))
    
    
print_your_name()