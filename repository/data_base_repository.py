import json
#Obtenemos la Data base 

def get_data() -> dict: 
    
    with open('archivos_json\data_base.json', 'r') as file:
        data_base = json.load(file)
        
    return  data_base

#Obtenemos un estudiante 

def get_student(name: str) -> dict | None:
    
    data = get_data()
    
    students = data["estudiantes"]
    
    if students is None or len(students) == 0 or name is None or name == "":
        return None
    
    result = None
    
    for student in students:
        if name == student["name"]:
            result = student
            break
        
    return result

#tenemos que obtener una materia


def get_subjets(name: str) -> dict | None:
    
    data = get_data()
    
    students = data["estudiantes"]
    
    if students is None or len(students) == 0 or name is None or name == "":
        return None
    
    result = None
    
    for student in students:
        if name == student["name"]:
            result = student
            break
        
    return result


def add_subjet(subjet: str, name: str) -> bool:
    
    student = get_student(name)
    
    wrapped_subjet = student["subjet"]
    wrapped_subjet[subjet] = {}
    student["subjet"] = wrapped_subjet
    
    result = update_student_in_db(student)
    return result



def add_task(task: str, subjet: str) -> bool:
    
    subjet = get_student(subjet)
    
    wrapped_task = subjet[0]
    wrapped_task[task] = {}
    subjet["subjet"] = wrapped_task
    
    result = update_student_in_db(subjet)
    return result
    
#Con esta opcion actualizamos al estudiante en la base de datos, Borramos el viejo, ponemos al nuevo        
def add_subjet2(subjet: str, name: str) -> bool:
    student = get_student(name)
    
    wrapped_subjet = student["materia"]
    wrapped_subjet[subjet] = {}
    student["materia"] = wrapped_subjet
            
def update_student_in_db(student: dict) ->bool:
    
    data = get_data()
    students = data["estudiantes"]
    
    for i in range(len(students)):
        if students[i]["name"] == student["name"]:
            
            students[i] = student
            break
        
    data["estudiantes"] = students
    
    
    
    try:
        data_str = json.dumps(data,indent=4)
        
        with open(r'C:\Users\cesar\OneDrive\Escritorio\Python\proyect_student_manager\archivos_json\data_base.json', 'w') as file:
            file.write(data_str)
            
        return True
    except:
        return False
    
        
    
    
