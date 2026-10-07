print("------Clasificador de Nivel Gamer-----")
name=(input("Ingresa tu nombre:  "))
hours=(int(input("Cuantas horas llevas jugando? ")))
is_competitive=input("juegas competitivo? (si/no):")
if hours<10:
    Category="Novato"
    message= "¡Bienvenidos al mundo Gamer!"
elif hours<50:
    Category="Casual"
    message="Ya le estás agarrando el ritmo"
elif hours<200:
    Category= "Gamer"
    message= "Definitivamente  sabes lo que haces"
elif hours >= 200 and is_competitive=="si":
    Category="Pro"
    message="Eres una leyenda viviente"
else:
    Category= "Gamer"
    message="Tienes la experiencia, pero aun no entras al competitivo"
print(f"{name}, tu categoria es: {Category}")
print(message)