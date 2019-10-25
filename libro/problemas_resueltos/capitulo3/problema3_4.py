NOM = 0
SUE = float(input("Introduce el sueldo del trabajador: "))
while(SUE != (-1)):
    if SUE < 1000:
        NSUE = SUE*1.15
    else:
        NSUE = SUE*1.12
    NOM = NOM + NSUE
    print(f"El nuevo sueldo del trabajador es ${NSUE}")
    SUE = float(input("Introduce el sueldo del trabajador: "))
else:
    print(f"El nuevo sueldo de los trabajadores es ${NOM}")

print("Fin del programa")
