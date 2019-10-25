TIPO1 = 0
TIPO2 = 0
TIPO3 = 0
TIPO4 = 0
TIPO5 = 0
MCTIPO2 = 0
N = int(input("Introduce el numero de años que se produjo vino: "))
for I in range(1, N+1, 1):
    TOTVIN = 0
    for J in range(1, 6, 1):
        V = float(input("Ingresa la cantidad de litros de vino producidos en el año: "))
        TOTVIN = TOTVIN + V
        if J == 1:
            TIPO1 = TIPO1+V
        elif J == 2:
            TIPO2 = TIPO2+V
            if V > MCTIPO2:
                MCTIPO2 = V
                AÑO = I
        elif J == 3:
            TIPO3 = TIPO3+V
            if V == 0:
                print(f"En el año {I} no se produjo vino tipo 3")
        elif J == 4:
            TIPO4 = TIPO4+V
        elif J == 5:
            TIPO5 = TIPO5+V
    else:
        print(f"El total de litros producidos en un año es {TOTVIN}")
else:
    print(f"El total de litros producidos del tipo 1 es {TIPO1}")
    print(f"El total de litros producidos del tipo 2 es {TIPO2}")
    print(f"El total de litros producidos del tipo 3 es {TIPO3}")
    print(f"El total de litros producidos del tipo 4 es {TIPO4}")
    print(f"El total de litros producidos del tipo 5 es {TIPO5}")
    print(f"El año {AÑO} fue en el que se produjo la mayor cantidad de vino tipo 2 y la cantidad de litros producidos del tipo 2 fue {MCTIPO2}")
print("Fin del programa")

