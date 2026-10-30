import csv


def student_info():
    student_data={}
    while True:
        try:
            student_name=str(input("Ingrese el nombre del estudiante: "))
            student_data['name']=student_name
            break
        except ValueError:
            print("Nombre inválido, intente de nuevo: ")
    while True:
        try:
            student_class=str(input("Ingrese la seccion del estudiante: "))
            student_data['class']=student_class
            break        
        except ValueError:
            print("Sección inválida, intente de nuevo: ")
    while True:
        try:
            spanish_grade=float(input("Ingrese la nota de español: "))
            if spanish_grade < 0 or spanish_grade > 100:
                raise ValueError
            else:
                student_data['spanish_grade']=spanish_grade
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            english_grade=float(input("Ingrese la nota de inglés: "))
            if english_grade < 0 or english_grade > 100:
                raise ValueError
            else:
                student_data['english_grade']=english_grade
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            social_studies_grade=float(input("Ingrese la nota de estudios sociales: "))
            if social_studies_grade < 0 or social_studies_grade > 100:
                raise ValueError
            else:
                student_data['social_studies_grade']=social_studies_grade
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            science_grade=float(input("Ingrese la nota de ciencias: "))
            if science_grade < 0 or science_grade > 100:
                raise ValueError
            else:
                student_data['science_grade']=science_grade
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    return student_data


def add_student(info,students):
    new_student=info
    student_list=students
    found= False
    for student in student_list:
        if student['name'] == new_student['name'] and student['class']==new_student['class']:
            found= True
    if found== False:
        student_list.append(new_student)
        print(f"Se agregó a el estudiante {new_student['name']}")
        return student_list
    else:
        print(f"El estudiante {new_student['name']}, ya se encuentra agregado")


def student_delete_info():
    student_data={}
    while True:
        try:
            student_name=str(input("Ingrese el nombre del estudiante que desea remover: "))
            student_data['name']=student_name
            break
        except ValueError:
            print("Nombre inválido, intente de nuevo: ")
    while True:
        try:
            student_class=str(input("Ingrese la seccion del estudiante que desea remover: "))
            student_data['class']=student_class
            break        
        except ValueError:
            print("Sección inválida, intente de nuevo: ")
    return student_data


def delete_student(student_to_delete,students):
    student_to_remove=student_to_delete
    student_list=students
    name_to_find=student_to_remove['name']
    class_to_find=student_to_remove['class']
    found= False
    for student in student_list:
        if student['name'] == student_to_remove['name'] and student['class']==student_to_remove['class']:
            found= True
    if found== True:
        for index, student in enumerate(student_list):    
            if student["name"] == name_to_find and student["class"] == class_to_find:
                student_list.pop(index)
        return student_list
    else:    
        print(f"El estudiante {name_to_find} de la sección {class_to_find}, no se encuentra en la lista de estudiantes")
        return students


def see_current_students(students):
    student_list=students
    for student in student_list:
        print(student)


def see_failed_students(students):
    student_list=students
    for student in student_list:
        if student["spanish_grade"]<60:
            print(f"El estudiante {student["name"]}, de la sección {student["class"]}, perdió la materia de español con una nota de {student["spanish_grade"]}")
        if student["english_grade"]<60:
            print(f"El estudiante {student["name"]}, de la sección {student["class"]}, perdió la materia de inglés con una nota de {student["english_grade"]}")
        if student["social_studies_grade"]<60:
            print(f"El estudiante {student["name"]}, de la sección {student["class"]}, perdió la materia de estudios sociales con una nota de {student["social_studies_grade"]}")
        if student["science_grade"]<60:
            print(f"El estudiante {student["name"]}, de la sección {student["class"]}, perdió la materia de ciencias con una nota de {student["science_grade"]}")


def avg_dicc(students):
    student_list=students
    avg_grades={}
    for student in student_list:
        avg=0
        avg=(student["spanish_grade"]+student["english_grade"]+student["social_studies_grade"]+student["science_grade"])/4
        avg_grades[student["name"]]=avg
    return avg_grades


def see_best_average_grades(avg_dicc):
    avg_grades=avg_dicc
    best_average_grade=0
    best_student=""
    second_best_average_grade=0
    second_best_student=""
    third_best_average_grade=0
    third_best_student=""
    for name,grade in avg_grades.items():
        if  grade > best_average_grade:
            third_best_average_grade=second_best_average_grade
            third_best_student=second_best_student
            second_best_average_grade=best_average_grade
            second_best_student=best_student
            best_average_grade= grade
            best_student=name
        elif grade > second_best_average_grade:
                third_best_average_grade=second_best_average_grade
                third_best_student=second_best_student
                second_best_average_grade=grade
                second_best_student=name
        elif grade > third_best_average_grade:
            third_best_average_grade=grade
            third_best_student=name
    print("El top 3 de mejores estudiantes es:")        
    print(F"En numero 3 el estudiante con la mejor nota promedio es {third_best_student}, con una nota promedio de {third_best_average_grade}")
    print(F"En numero 2 el estudiante con la mejor nota promedio es {second_best_student}, con una nota promedio de {second_best_average_grade}")
    print(F"Y en numero 1 El estudiante con la mejor nota promedio es {best_student}, con una nota promedio de {best_average_grade}")


def see_all_average_grades(avg_dicc):
    avg_grades=avg_dicc
    for student,grade in avg_grades.items():
        print(f"El estudiante {student}, tiene una nota promedio de {grade}.")