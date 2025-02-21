##### Obtener estudiante por nombre:
import json

def get_data() -> dict: 
    
    with open('archivos_json\data_base.json', 'r') as file:
        data_base = json.load(file)
        return data_base
       
def get_student_by_name(data,students: list, name: str) -> dict | None:
    if not students or not name:
        return None
    
    for student in students:
        if name.lower() == student["name"].lower():  # Ignora mayúsculas/minúsculas
            print("El estudiante ya está registrado.")
            return student
        
        else:

            print("Estudiante nuevo registrado.")
            subject = str(input("Registre una materia: "))
            task = str(input("Restre una tarea:"))
            grades = int(input("Registre una nota:"))
            new_student = {
                    "name": name,
                    "subject":  {
                        subject: {
                            "task": {
                                task: [grades]
                            }
                        }
                    }
                }
            
            data["estudiantes"].append(new_student)
            data_str = json.dumps(data,indent=4)
            
            with open(r'C:\Users\cesar\OneDrive\Escritorio\Python\proyect_student_manager\archivos_json\data_base.json', 'w') as file:
                file.write(data_str)
            
            print("muero aqui 1")
            print("muero aqui 2")
            return new_student
        
        
    
        
    
      
        
        
      
     

    

    

