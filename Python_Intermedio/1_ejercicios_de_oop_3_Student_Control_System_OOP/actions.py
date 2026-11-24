from student import Student

def student_info():
    student_name=str(input("Ingrese el nombre del estudiante: "))
    student_class=str(input("Ingrese la seccion del estudiante: "))
    while True:
        try:
            spanish_grade=float(input("Ingrese la nota de español: "))
            if spanish_grade < 0 or spanish_grade > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            english_grade=float(input("Ingrese la nota de inglés: "))
            if english_grade < 0 or english_grade > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            social_studies_grade=float(input("Ingrese la nota de estudios sociales: "))
            if social_studies_grade < 0 or social_studies_grade > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    while True:
        try:
            science_grade=float(input("Ingrese la nota de ciencias: "))
            if science_grade < 0 or science_grade > 100:
                raise ValueError
            else:
                break
        except ValueError:
            print("Nota inválida intente de nuevo: ")
    return Student(student_name, student_class, spanish_grade, english_grade, social_studies_grade, science_grade)


def add_student(info,students):
    new_student=info
    student_list=students
    found= False
    for student in student_list:
        if student.name == new_student.name and student.section == new_student.section :
            found= True
    if found== False:
        student_list.append(new_student)
        print(f"Se agregó a el estudiante {new_student.name}")
    else:
        print(f"El estudiante {new_student.name}, ya se encuentra agregado")


def student_delete_info():
    student_name=str(input("Ingrese el nombre del estudiante que desea remover: "))
    student_class=str(input("Ingrese la seccion del estudiante que desea remover: "))
    return student_name, student_class


def delete_student(student_name, section, students):
    found = False
    for index, student in enumerate(students):
        if student.name == student_name and student.section == section:
            students.pop(index)
            found = True
            break
    if found:
        print(f"El estudiante {student_name} de la sección {section}, fue removido de la lista de estudiantes")
    else:
        print(f"El estudiante {student_name} de la sección {section}, no se encuentra en la lista de estudiantes")


def see_current_students(students):
    student_list=students
    for student in student_list:
        print(f"Nombre: {student.name}, sección: {student.section}, Nota de español: {student.spanish_grade}, Nota de inglés: {student.english_grade}, Nota de estudios sociales: {student.social_studies_grade}, Nota de ciencias: {student.science_grade}")


def see_failed_students(students):
    student_list=students
    for student in student_list:
        if student.spanish_grade<60:
            print(f"El estudiante {student.name}, de la sección {student.section}, perdió la materia de español con una nota de {student.spanish_grade}")
        if student.english_grade<60:
            print(f"El estudiante {student.name}, de la sección {student.section}, perdió la materia de inglés con una nota de {student.english_grade}")
        if student.social_studies_grade<60:
            print(f"El estudiante {student.name}, de la sección {student.section}, perdió la materia de estudios sociales con una nota de {student.social_studies_grade}")
        if student.science_grade<60:
            print(f"El estudiante {student.name}, de la sección {student.section}, perdió la materia de ciencias con una nota de {student.science_grade}")

def avg_students_list (students):
    student_list=students
    avg_grades={}
    for student in student_list:
        avg=student.get_average()
        avg_grades[(student.name, student.section)] = avg
    return avg_grades


def see_best_average_grades(avg_students_list):
    avg_grades=avg_students_list
    best_average_grade=0
    best_student=""
    second_best_average_grade=0
    second_best_student=""
    third_best_average_grade=0
    third_best_student=""
    for (name, section), grade in avg_grades.items():
        if  grade > best_average_grade:
            third_best_average_grade=second_best_average_grade
            third_best_student=second_best_student
            second_best_average_grade=best_average_grade
            second_best_student=best_student
            best_average_grade= grade
            best_student=f"{name}, sección {section}"
        elif grade > second_best_average_grade:
            third_best_average_grade=second_best_average_grade
            third_best_student=second_best_student
            second_best_average_grade=grade
            second_best_student=f"{name}, sección {section}"
        elif grade > third_best_average_grade:
            third_best_average_grade=grade
            third_best_student=f"{name}, sección {section}"
    print("El top 3 de mejores estudiantes es:")        
    print(F"En numero 3 el estudiante con la mejor nota promedio es {third_best_student}, con una nota promedio de {third_best_average_grade}")
    print(F"En numero 2 el estudiante con la mejor nota promedio es {second_best_student}, con una nota promedio de {second_best_average_grade}")
    print(F"Y en numero 1 El estudiante con la mejor nota promedio es {best_student}, con una nota promedio de {best_average_grade}")


def see_all_average_grades(avg_students_list):
    avg_grades=avg_students_list
    for (name, section),grade in avg_grades.items():
            print(f"El estudiante {name}, tiene una nota promedio de {section}.")