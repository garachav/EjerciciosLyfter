#2. Agrupar empleados por departamento
#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},]


employees_by_department = {}

for employee in employees:
    department = employee['department']
    name = employee['name']
    if department in employees_by_department:
        employees_by_department[department].append(name)
    else:
        employees_by_department[department] = [name]

print(employees_by_department)

print(name)