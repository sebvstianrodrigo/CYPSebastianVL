MAT = int(input("Introduce la matricula del alumno: "))
CAL1 = float(input("Introduce la primera calificacion del alumno: "))
CAL2 = float(input("Introduce la segunda calificacion del alumno: "))
CAL3 = float(input("Introduce la tercera calificacion del alumno: "))
CAL4 = float(input("Introduce la cuarta calificacion del alumno: "))
CAL5 = float(input("Introduce la quinta calificacion del alumno: "))
PRO = (CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO >= 6:
    print(f"La matricula del alumno es {MAT} y su promedio es de {PRO} asi que esta aprobado")
else:
    print(f"La matricula del alumno es {MAT} y su promedio es de {PRO} asi que no esta aprobado")

print("Fin del programa")

