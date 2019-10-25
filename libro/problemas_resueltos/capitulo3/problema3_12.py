MASUE = 0
N = int(input("Introduce el numero de empleados: "))
for i in range(0, N, 1):
    NUMEMP = int(input("Introduce el numero de empleado: "))
    SUE = float(input("Introduce el sueldo del empleado: "))
    if SUE > MASUE:
        MASUE = SUE
        MANUM = NUMEMP
else:
    print(f"El numero de empleado con mayor sueldo es {MANUM} y el mayor sueldo de los empleados es ${MASUE}")

print("Fin del programa")

