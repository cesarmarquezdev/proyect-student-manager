import json
from services.student_service import get_student_by_name
from repository.data_base_repository import get_data, add_subjet, add_task


"""{
    "estudiantes": [
        {
            "name": "ana",
            "subjet": {
                "Matemáticas": {
                    "tareas": {
                        "Examen 1": [15, 18]
                    }
                }
            }
        }
    ]
}"""


def section_one():

    data = get_data()
    students = data["estudiantes"]
       
    name = str(input("ingrese el nombre en el usuario: "))
    student = get_student_by_name(data,students, name)
    
    if student is not None:
        
            opcion = int(input("""
        --- Gestor de Estudiantes Avanzado ---
1. Agregar estudiante/materia/tarea
2. Mostrar promedios por materia
3. Mostrar notas de una materia
4. Salir  """))
            
            
            if opcion == 1:
                second_opcion = "s"
                while second_opcion == "s":
                
                    subjet = str(input("Introduzca la materia: "))
                    add_subjet_result = add_subjet(subjet,name) 
                    if add_subjet_result:
                        print("tu materia fue agregada exitosamente")
                    else:
                        print("No se pudo agregar la materia")
                        
                    second_opcion = str(input("Desea agregar otra materia? S/N: "))
            
            
            if opcion == 2:
                second_opcion = "s"
                while second_opcion == "s":
                    subjet = str(input("Introduzca la materia a la cual desea agregarle una tarea: "))
                    task = str(input("Introduzca el nombre de la tarea: "))
                    add_task_result = add_task(task,subjet)
                    if add_task_result:
                        print("tu tarea fue agregada exitosamente")
                    else:
                        print("No se pudo agregar la tarea")
                        
                    second_opcion = str(input("Desea agregar otra tarea? S/N: "))
            
            
            if opcion ==3:
                second_opcion = "s"
                while second_opcion =="s":
                    task = str(input("A cual evaluacion  desea agregar la nota?"))
#Cambio para probar el commit 
#hacidnfo pruebas 
                    


section_one()


