MED = 0
CHI = 0
GRA = 0
N = int(input("Introduce el numero de ventas del vendedor: "))
for i in range(0, N, 1):
    V = float(input("Introduce la venta del vendedor: "))
    if V <= 200:
        CHI = CHI + 1
    elif V < 400:
        MED = MED + 1
    else:
        GRA = GRA + 1

else:
    print(f"El numero de ventas menores a $200 son {CHI}, menores a $400 son {MED} y mayores a $400 son {GRA}")

print("Fin del programa")
