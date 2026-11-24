import csv
from student import Student

def import_data_csv(file_path,students):
    student_list=[]
    try:
        with open(file_path,'r', encoding='utf-8')as file:
            reader=csv.DictReader(file)
            for student in reader:
                new_student= Student(student["name"],student["class"],float(student["spanish_grade"]),float(student["english_grade"]), float(student["social_studies_grade"]),float(student["science_grade"]))
                student_list.append(new_student)
        print(f"Se importaron {len(student_list)} estudiantes del CSV correctamente")
        return student_list
    except FileNotFoundError:
        print(f"El archivo csv llamado {file_path}, no existe")
        return students
    

def export_data_csv(file_path,students):
    student_list=[]
    for student in students:
        student_list.append(student.to_dict())
    with open(file_path,'w', encoding='utf-8', newline='')as file:
        headers = ["name", "class", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"]
        writer=csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(student_list)
    print("Se exportó la información al CSV correctamente")