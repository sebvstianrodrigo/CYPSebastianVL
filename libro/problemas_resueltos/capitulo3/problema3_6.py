MAY = -100000
MEN = 100000
N = int(input("Ingresa un numero entero: "))
for i in range(0, N, 1):
    NUM = int(input("Ingresa un numero entero: "))
    if NUM > MAY:
        MAY = NUM
    else:
        if NUM < MEN:
            MEN = NUM
    
else:
    print(f"El maximo valor es {MAY} y el minimo valor es {MEN}")
print("Fin del programa")
