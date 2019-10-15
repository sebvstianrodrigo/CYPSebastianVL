A = int(input("Introduce un numero entero: "))
B = int(input("Introduce otro numero entero: "))
C = int(input("Introduce otro numero entero: "))
if A < B:
    if B < C:
        print(f"Los numeros {A}, {B} y {C} estan en orden creciente")
    else:
        print(f"Los numeros {A}, {B} y {C} no estan en orden creciente")
else:
    print(f"Los numeros {A}, {B} y {C} no estan en orden creciente")

print("Fin del programa")

