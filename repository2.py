import json

# 📂 Ruta del archivo JSON
FILE_PATH = r'C:\Users\cesar\python\proyect_student_manager\archivos_json\estudiantes.json'

def get_data() -> dict:
    """Lee y devuelve los datos del archivo JSON."""
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def update_student_in_db(student: dict) -> bool:
    """Actualiza la información de un estudiante en la base de datos y guarda los cambios."""
    data = get_data()
    students = data["estudiantes"]

    for i in range(len(students)):
        if students[i]["nombre"] == student["nombre"]:
            students[i] = student
            break

    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"❌ Error al guardar datos: {e}")
        return False
    
def get_data() -> dict:  
 
    with open('archivos_json/estudiantes.json', 'r') as file:
        return json.load(file)
    
def get_student(name: str) -> dict | None:
    
    data = get_data()
    
    students = data["estudiantes"]
    
    if students is None or len(students) == 0 or name is None or name == "":
        return None
    
    result = None
    
    for student in students:
        if name == student["nombre"]:
            result = student
            break
        
    return result
  
def get_student_by_name(name: str,students: list) ->dict:
    for student in students:
        
        if name.lower() == student["nombre"].lower():
            print("el estudiante ya esta registrado")
            return student

    print("el estudiante nuevo registrado") #Cambiarr print 
    #Agregar validacion 
    add_student(name) 
        
def update_student_in_db(student: dict) ->bool:
    
    data = get_data()
    students = data["estudiantes"]
    
    for i in range(len(students)):
        
        if students[i]["nombre"] == student["nombre"]:
            
            students[i] = student
            break
        
    data["estudiantes"] = students
    
    
    
    try:
        data_str = json.dumps(data,indent=4)
        
        with open(r'C:\Users\cesar\python\proyect_student_manager\archivos_json\estudiantes.json', 'w') as file:
            file.write(data_str)
            
        return True
    except:
        return False

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
    





#Esto tiene que ir en la capa de servicio.

