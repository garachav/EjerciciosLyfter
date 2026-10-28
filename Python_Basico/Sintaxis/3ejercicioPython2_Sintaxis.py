name=(input("ingresa tu nombre completo: "))
age=int(input("Ingresa tu edad: "))
if age<=4:
    stage="bebé"
elif age>4 and age<=11:
    stage="niño"
elif age>11 and  age<=14:
    stage="preadolescente"
elif age>14 and age<=17:
    stage="adolescente"
elif age>17 and age<=25:
    stage="adulto joven"
elif age>25 and age<=60:
    stage= "adulto"
else:
    stage= "adulto mayor"
print(f"Hola {name } tu edad es de {age } y estas en la etapa de {stage} de tu vida")
