time=float(input("Digite el tiempo en segundos:"))
while time<0:
    time=float(input(" Tiempo incorrecto,digite el tiempo en segundos:"))
if time<600:
    print(f"Le faltan {600-time} segundos para 10 minutos.")
elif time==600:
    print("Igual")
else:
    print("Mayor")
