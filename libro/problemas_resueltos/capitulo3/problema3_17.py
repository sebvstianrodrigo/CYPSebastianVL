I = 3
SP = 0
M = int(input("Introduce un numero entero: "))
if M >= 1:
    SP = SP + 1
    print("El numero primo es:", 1)
    if M >= 2:
        SP = SP + 1
        print("El numero primo es:", 2)
while I <= M:
    BAND = 'V'
    J = 3
    while (J < (I / 2)) and (BAND == 'V'):
        if (I % J) == 0:
            BAND = 'F'
        J = J+2
    if (BAND == 'V'):
        print("El numero primo es:", I)
        SP = SP + 1
    I = I+2

print(f"Entre 1 y {M} hay {SP} numeros primos")
print("Fin del programa")
