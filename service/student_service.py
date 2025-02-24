from repository2 import get_data, update_student_in_db
import json

def add_task(subject: str, task: str, name: str) -> bool:
    """Agrega una tarea a un a una materia."""
    if not task:
        print("El nombre de La tarea no es valida")
        return False
    data = get_data()
    students = data["estudiantes"]
    
    for student in students:
        if student["nombre"].lower() == name.lower():
            # Asegurar que "materias" sea un diccionario
            if not isinstance(student.get("materias"), dict):
                student["materias"] = {}


            # Agregar la nueva materia si no existe
            task_objet = {task: ""}
            
            if subject not in student["materias"]:
                student["materias"][subject] = {
                    "task": task_objet
                }
              
            else:
                student["materias"][subject]["task"][task]= ""
                

            if update_student_in_db(student):
                print(f" tarea '{task}' agregada a '{subject}'.")
            else:
                print("Hubo un error")

            return True

    print(f" El estudiante '{name}' no fue encontrado.")
    
def add_grade(subject: str, task: str, name: str,grade: str) -> bool:

    """Agrega una tarea a un a una notaa."""
    if not grade:
        print("El nombre de La nota no es valida")
        return False
    data = get_data()
    students = data["estudiantes"]
    
    for student in students:
        if student["nombre"].lower() == name.lower():
            # Asegurar que "materias" sea un diccionario
            if not isinstance(student.get("materias"), dict):
                student["materias"] = {
                    "task": {
                        task: grade
                    }}
             
            # Agregar la nueva materia si no existe
            student["materias"][subject]["task"][task] = grade

            if update_student_in_db(student):
                print(f" tarea '{task}' agregada a '{subject}'.")
            else:
                print("Hubo un error")

            return True

    print(f" El estudiante '{name}' no fue encontrado.")
    
def add_subject_simple(name: str, subject: str) -> bool:
    """Agrega una materia a un estudiante."""
    if  not subject:
        print("El nombre de la materia no es valida")
        return False
    
    data = get_data()
    students = data["estudiantes"]
    
    for student in students:
        if student["nombre"].lower() == name.lower():
            # Asegurar que "materias" sea un diccionario
            if not isinstance(student.get("materias"), dict):
                student["materias"] = {}

            # Agregar la nueva materia si no existe
            if subject not in student["materias"]:
                student["materias"][subject] = {
                    "task": {
                        
                    }
                }
                
                if update_student_in_db(student):
                    print(f" Materia '{subject}' agregada a '{name}'.")
                else:
                    print("Hubo un error")
                    
            else:
                print(f" '{name}' ya tiene la materia '{subject}' registrada.")
     
            return True
    
    print(f" El estudiante '{name}' no fue encontrado.") 

def add_student(name: str) -> bool:
    
    if not name:
        print("Nombre del estudiante no valido ingrese un nombre valido ")
        return
    data=get_data()
    
    new_student =  {
        "nombre": name  #Cambiar propiedades 
    }
#Implementar try cath
    data["estudiantes"].append(new_student)
    data_str = json.dumps(data,indent=4)
            
    with open(r'C:\Users\cesar\python\proyect_student_manager\archivos_json\estudiantes.json', 'w') as file:
        file.write(data_str)
    

