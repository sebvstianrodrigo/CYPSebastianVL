N = int(input("Introduce el numero de sonidos emitidos por un grillo en un minuto: "))
T = 0
if N > 0:
    T = N / 4 + 40
    print(f"La temperatura en grados Fahrenheit es {T}")
    print("Fin del programa")
else:
    print("Fin del programa")
