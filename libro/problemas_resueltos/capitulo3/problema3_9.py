SERIE = 0
N = int(input("Introduce el numero de terminos de la serie: "))
for i in range(1, N, 1):
    SERIE = SERIE + i**i
else:
    print(f"El resultado de la serie es {SERIE}")
print("Fin del programa")
