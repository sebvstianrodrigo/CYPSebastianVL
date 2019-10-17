SUE = float(input("Introduce el sueldo del trabajador:"))
if SUE<1000:
    NSUE = SUE * 1.15
    print(f"El nuevo sueldo del trabajador es ${NSUE}")
else:
    NSUE = SUE * 1.12
    print(f"El nuevo sueldo del trabajador es ${NSUE}")

