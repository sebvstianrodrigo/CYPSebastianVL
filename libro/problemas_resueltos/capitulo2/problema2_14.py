TIPOENF = int(input("Introduce el tipo de enfermedad del paciente: "))
EDAD = int(input("Ingresa la edad del paciente: "))
DIAS = int(input("Ingresa el numero de dias que el paciente estuvo hospitalizado: "))
if TIPOENF == 1:
    COSTOT = DIAS*25
if TIPOENF == 2:
    COSTOT = DIAS*16
if TIPOENF == 3:
    COSTOT = DIAS*20
if TIPOENF == 4:
    COSTOT = DIAS*32

if EDAD >= 14:
    if EDAD <= 22:
        COSTOT = COSTOT*1.10
        print(f"El costo total del paciente es ${COSTOT}")
    else:
        print(f"El costo total del paciente es ${COSTOT}")
else:
    print(f"El costo total del paciente es ${COSTOT}")

print("Fin del programa")
