NUM = int(input("Introduce un numero entero: "))
if NUM > 0:
    while(NUM != 1):
        print(NUM)
        if (-1) ** NUM > 0:
            NUM = NUM / 2
        else:
            NUM = (NUM*3) + 1
    else:
        print(NUM)
else:
    print("El numero tiene que ser un entero positivo")

print("Fin del programa")
