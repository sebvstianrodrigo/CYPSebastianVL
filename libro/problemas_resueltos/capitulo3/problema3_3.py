SERIE = 0
N = int(input("Introduce un numero entero: "))
BAND = 'T'
for i in range(1, N, 1):
    if BAND == 'T':
        SERIE = SERIE + 1/i
        BAND = 'F'
    else:
        SERIE = SERIE - 1/i
        BAND = 'T'
else:
    print(f"El resultado es {SERIE}")

print("Fin del programa")
