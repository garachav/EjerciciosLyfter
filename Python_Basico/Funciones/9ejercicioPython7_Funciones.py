#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). +
# Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
numero=8
print(is_prime(numero))



def get_primes(numbers):
    prime_list = []
    for juan in numbers:
        if is_prime(juan):
            prime_list.append(juan)
    return prime_list

ejemplo=[1, 4, 6, 7, 13, 9, 67]
print(get_primes([4,8,12]))
print(get_primes(ejemplo))
print(is_prime(9))