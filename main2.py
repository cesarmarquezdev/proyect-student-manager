import json
from repository2 import get_data,get_student_by_name, get_student, update_student_in_db
from service.student_service import add_task,add_grade,add_subject_simple
data = get_data()
students = data["estudiantes"]
final_check ="s"
while final_check == "s":
    print("""--- Gestor de Estudiantes Avanzado ---
1. Agregar estudiante/materia/tarea
2. Mostrar promedios por materia
3. Mostrar notas de una materia
4. Salir""")

            
    loop_check = "s"

    while loop_check == "s":
        option = input("Seleccione una opción 1, 2, 3 o 4): ").strip()
        if not option.isdigit() or option not in {"1", "2", "3", "4"}:
            print("Opcion no valida. Intente de nuevo: ")
            continue
        option = int(option)

        if option == 1:
            
            name = str(input("Introduzca el Nombre del estudiante: "))
            get_student_by_name(name,students)
            check_option_1 = "s"
            while check_option_1 == "s":
                subject = str(input("Nombre de la materia: "))
                add_subject_result = add_subject_simple(name,subject)
                if add_subject_result:
                    check_option_2 = "s"
                    while check_option_2 == "s":
                        
                        task = str(input("agregar una tarea: "))
                        add_task_result = add_task(subject,task,name)
                        if add_task_result:
                            check_option_3 = "s"
                            while check_option_3 == "s":
                                grade = str(input("agregar grade: "))
                                add_grade(subject,task,name,grade)
                                check_option_3 = str(input("Desea registrar otro grade  S/N: ")).lower()
                            
                        check_option_2 = str(input("Desea registrar otra tarea  S/N: ")).lower()
                
                check_option_1 = str(input("Desea registrar otra materia  S/N: ")).lower()
                
        if option == 2:
            name = str(input("Introduzca el Nombre del estudiante: "))
            student = get_student_by_name(name,students)
            subjects = student["materias"]
            result = {}
            
            for subject_key, subject_value in subjects.items():
                total_grades = 0
                total_task = 0
                
                for grade_key, grade_value in subject_value["task"].items():
                    total_task += 1
                    
                    if not grade_value:
                        continue
                    
                    total_grades += int(grade_value)
                
                result[subject_key] =  total_grades / total_task
                
            print(result)
        
        if option == 3:
            name = str(input("Introduzca el Nombre del estudiante: "))
            student = get_student_by_name(name,students)
            subjects = student["materias"]
            for subject in subjects:
                print(subject)
            subject_input = str(input("Introduce la materia que quieras consultar: "))
            
            for subject_key, subject_value in subjects.items():
                if subject_key == subject_input:
                    for grade_key, grade_value in subject_value["task"].items():
                        print(grade_key,grade_value)
                
        if option == 4:
            loop_check = "n"
            final_check = "n"
        loop_check = str(input("Desa continuar en el programa s/n: "))
                    

                
        
        
        

        

