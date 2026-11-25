def operation ():
    action=0
    while True:
        try:
            action=int(input(f"Seleccione: 1 para Ingresar un estudiante,2 para eliminar un estudiante,3 para Ver información de estudiantes ingresados,4 Ver estudiantes reprobados,5 para Ver el top 3 de los estudiantes con la mejor nota promedio,6 Ver la nota promedio entre las notas de todos los estudiantes,7 para Importar datos de CSV,8 para Exportar datos a CSV,9 Salir: "))
            if action<1 or action>9: 
                raise ValueError()
            return action
        except ValueError as e:
            print("Opción no válida, intente de nuevo")