MAT = int(input("Introduce la matricula del alumno: "))
CARR = str(input("Ingresa la carrera que inscribio el alumno: "))
SEM = int(input("Introduce el semestre que el alumno tiene aprobado: "))
PROM = float(input("Introduce el promedio del alumno: "))
if CARR == "Economia":
    if SEM >= 6:
        if PROM >= 8.8:
            print(f"La matricula del alumno es {MAT} y fue aceptado en {CARR}")
        else:
            print("El alumno fue rechazado")
    else:
        print("El alumno fue rechazado")
if CARR == "Computacion":
    if SEM > 6:
        if PROM > 8.5:
            print(f"La matricula del alumno es {MAT} y fue aceptado en {CARR}")
        else:
            print("El alumno fue rechazado")
    else:
        print("El alumno fue rechazado")
if CARR == "Contabilidad":
    if SEM > 5:
        if PROM > 8.5:
            print(f"La matricula del alumno es {MAT} y fue aceptado en {CARR}")
        else:
            print("El alumno fue rechazado")
    else:
        print("El alumno fue rechazado")
if CARR == "Administracion":
    if SEM > 5:
        if PROM > 8.5:
            print(f"La matricula del alumno es {MAT} y fue aceptado en {CARR}")
        else:
            print("El alumno fue rechazado")
    else:
        print("El alumno fue rechazado")

print("Fin del programa")
