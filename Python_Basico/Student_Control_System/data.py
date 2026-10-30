import csv


def import_data_csv(file_path,students):
    student_list=[]
    try:
        with open(file_path,'r', encoding='utf-8')as file:
            reader=csv.DictReader(file)
            for student in reader:
                student["name"] = str(student["name"])
                student["class"] = str(student["class"])
                student["spanish_grade"] = float(student["spanish_grade"])
                student["english_grade"] = float(student["english_grade"])
                student["social_studies_grade"] = float(student["social_studies_grade"])
                student["science_grade"] = float(student["science_grade"])
                student_list.append(student)
        print(f"Se importaron {len(student_list)} estudiantes del CSV correctamente")
        return student_list
    except FileNotFoundError:
        print(f"El archivo csv llamado {file_path}, no existe")
        return students
    

def export_data_csv(file_path,students):
    student_list=students
    with open(file_path,'w', encoding='utf-8', newline='')as file:
        headers=student_list[0].keys()
        writer=csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(student_list)
    print("Se exportó la información al CSV correctamente")