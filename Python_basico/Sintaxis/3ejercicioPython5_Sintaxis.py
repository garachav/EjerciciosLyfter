quantity=(int(input("¿Cuantas notas vamos a revisar? ")))
counter=1
approved=0
failed=0
sum_approved=0
sum_failed=0
grade=0
while counter <= quantity:
    grade=(int(input(f"Ingrese su nota {counter}: ")))
    if(grade>100 or grade<0):
        print("Nota no permitida, pongase serio")
    else:
        if(grade>=70):
            sum_approved=sum_approved+grade
            approved=approved+1
        else:
            sum_failed=sum_failed+grade
            failed=failed+1
        counter=counter+1
if(approved>0 and failed>0):
    print(f"De las {quantity} notas revisadas, usted ganó {approved} con un promedio de {sum_approved/approved} y perdió {failed} notas con un promedio de {sum_failed/failed}, el promedio total es de {(sum_approved+sum_failed)/(quantity)} ")
elif failed==0 :
    print(f"De las {quantity} notas revisadas, usted ganó todas las {quantity}!! con un promedio de {sum_approved/approved} ")
else: 
    print(f"De las {quantity} notas revisadas, usted perdió todas las {quantity} con un promedio de {sum_failed/quantity}")