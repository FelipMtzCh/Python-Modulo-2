# Lista global donde se almacenan todos los alumnos
lista = []

def AregarAlumno() :
    alumnos = 0 # Contador de alumnos registrados
    nuevoAlumno = True # Controla si se siguen agregando alumnos

    while nuevoAlumno :
        print("Ingrese la opción deseada")
        opcionAlumno = input("Agregar alumno (1) o terminar (2): ")

        if opcionAlumno == "1" :
            # Solicita el nombre y lo formatea con mayúscula inicial
            nombre = input("Ingrese el nombre del alumno: ").title()
            # Se crea una lista donde el primer elemento es el nombre
            alumno = [nombre]
            # Se agregan las calificaciones al alumno
            AgregarCalificacion(alumno)
            # Se guarda el alumno en la lista global
            lista.append(alumno)
            alumnos += 1 # Incrementa el contador
        elif opcionAlumno == "2" :
            # Finaliza el registro de alumnos
            print(f"El programa ha terminado con {alumnos} alumno(s).")
            nuevoAlumno = False
            break
        else :
            # Manejo de opción inválida
            print("Se ha ingresado una opción no valida.")
            continue

def AgregarCalificacion(alumno) :
    calificacion1_valida = False # Controla la validación de la primera calificación

    # Solicita la primera calificación hasta que sea válida
    while calificacion1_valida == False :
        calificacion1 = input(f"Ingrese la primera calificación de {alumno[0]}: ")

        # Valida y agrega la calificación
        calificacion1_valida = ValidaCalificacion(alumno, calificacion1)
        if calificacion1_valida :

            nueva_calificacion = True # Controla si se agregan más calificaciones
            calificaciones = 1 # Contador de calificaciones

            # Permite agregar hasta 3 calificaciones
            while nueva_calificacion and calificaciones < 3 :
                print("Ingrese la opción deseada")
                opcionCalificacion = input("Agregar otra calificación (1) o terminar (2): ")

                if opcionCalificacion == "1" :
                    calificacion_correcta = False

                    # Solicita otra calificación hasta que sea válida
                    while calificacion_correcta == False :
                        calificacion = input(f"Ingrese la siguiente calificación de {alumno[0]}: ")
                        calificacion_correcta = ValidaCalificacion(alumno, calificacion)
                        if calificacion_correcta :
                            calificaciones += 1 # Incrementa el contador

                elif opcionCalificacion == "2" :
                    # Finaliza el ingreso de calificaciones
                    nueva_calificacion = False
                else :
                    print("Se ha ingresado una opción no valida.")
                    continue
        else :
            continue

def ValidaCalificacion(alumno, calificacion) :
    # Verifica que la entrada sea numérica
    if calificacion.isnumeric() :
        num_calificacion = int(calificacion)

        # Valida que esté en el rango permitido (5 a 10)
        if num_calificacion >= 5 and num_calificacion <= 10 :
            alumno.append(num_calificacion) # Agrega la calificación al alumno
            return True
        else :
            print("La calificación ingresada no es valida")
            return False
    else :
        # Mensaje si no se ingresó un número
        print(f"Por favor ingrese la calificación de {alumno[0]}")
        return False

def VerAlumnos(lista) :
    # Recorre la lista de alumnos
    for alumno in lista :
        total_calificaciones = len(alumno) - 1 # Total de calificaciones
        promedio = 0 # Acumulador del promedio
        calificaciones = "" # Cadena para mostrar calificaciones

        # Suma calificaciones y las guarda en texto
        for cal in alumno[1:] :
            promedio += cal
            calificaciones += f", {cal}" 
        
        # Calcula el promedio (división entera)
        promedio = promedio // total_calificaciones
        # Muestra los resultados del alumno
        print(f"El alumno {alumno[0]} tuvo las calificaciones{calificaciones} su promedio final es de {promedio}")

# Ejecución del programa
AregarAlumno()
VerAlumnos(lista)

