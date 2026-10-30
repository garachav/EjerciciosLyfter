# Cree un programa que:

# Pida al usuario su nombre
    # Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
# Luego pida su edad
    # Si no es un número válido, capture el ValueError y muestre un mensaje
# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"


def name ():
    name="No se ha indicado el nombre"
    while True:
        try:
            name=str(input("Ingrese su nombre: "))
            if name.isdigit():
                raise ValueError()
            return name
        except ValueError as e:
            print(f"El nombre no puede ser un número. ")    


def age():
    age=0
    while True:
        try:
            age=(input("Ingrese su edad: "))
            if age.isdigit():
                return age
            else:
                raise ValueError()
        except ValueError as e:
            print(f"Edad no valida. Detalles: ")    


def main ():
    print(f"Hola {name()}, su edad es {age()}")
    

if __name__ == '__main__':
    main()