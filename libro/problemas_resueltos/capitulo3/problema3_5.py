SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Introduce un numero entero: "))
for i in range(0, N, 1):
    NUM = int(input("Introduce un numero entero: "))
    if NUM > 0:
        SUMPOS = SUMPOS + NUM
        CUEPOS = CUEPOS + 1
    else:
        SUMOTR = SUMOTR + NUM
else:
    PROGEN = (SUMPOS+SUMOTR)/N
    PROPOS = (SUMPOS/CUEPOS)
    print(f"Los numeros positivos son {CUEPOS}, el promedio de los numeros positivos es {PROPOS} y el promedio general de los numeros es {PROGEN}")

print("Fin del programa")
