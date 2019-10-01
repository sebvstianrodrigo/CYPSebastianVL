SUE = float(input("Introduce el sueldo del trabajador:"))
if SUE < 1000:
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"El nuevo sueldo del trabajador es ${NSUE}")
else:
    print("fin del programa")
