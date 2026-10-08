# Cree una calculadora por linea de comando. 
# Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.PP

        #No es necesario:
        # def currentnumber ():
        #     current_number=0
        #     try:
        #         current_number=int(input("Seleccione el numero al que desea hacerle una operacion matematica: "))
        #         return current_number
        #     except ValueError as e: 
        #         print(f"Error [ValueError]: No se pudo convertir el valor 'abc' a un entero. Detalles: {e}")


def operation ():
    action=0
    while True:
        try:
            action=int(input("Seleccione: 1 para Suma, 2 para Resta, 3 para Multiplicación, 4 para División, 5 Borrar resultado, 6 Salir:  "))
            if action<1 or action>6: 
                raise ValueError()
            return action
        except ValueError as e:
            print(f"Error [ValueError]: Opcion no valida. Detalles: {e}")


def your_number():
    number=0
    while True:
        try:
            number=int(input("Seleccione el otro numero: "))
            return number
        except ValueError as e:
            print(f"Error [ValueError]: No se pudo convertir el valor 'abc' a un entero. Detalles: {e}")


def calculator (current_number,action,number):    
    if action== 1:
        result=current_number + number
    elif action== 2:
        result=current_number - number
    elif action== 3:
        result=current_number * number
    else:
        try:
            result=current_number / number
        except ZeroDivisionError as e:
            print(f"Error [ZeroDivisionError]: No se puede dividir entre 0. Detalles: {e}")
            return current_number
    print(f"El resultado es {result}")
    return result


def main():
    current_number=0
    while True:
        print(f"Número actual: {current_number}")
        option=operation ()
        if option==5:
            current_number=0
        elif option == 6:
            print("Adiós. ")
            break
        else:
            number= your_number()
            current_number=calculator(current_number,option,number)

if __name__ == '__main__':
    main()