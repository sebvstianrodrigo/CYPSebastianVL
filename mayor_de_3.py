NUM1 = int(input("Introduce el primer numero:"))
NUM2 = int(input("Introduce el segundo numero:"))
NUM3 = int(input("Introduce el tercer numero:"))
if NUM1 > NUM2 and NUM1 > NUM3:
    print(f"{NUM1} es el numero mayor")
if NUM2 > NUM1 and NUM2 > NUM3:
    print(f"{NUM2} es el numero mayor")
if NUM3 > NUM2 and NUM3 > NUM1:
    print(f"{NUM3} es el numero mayor")

print("Otra solucion")
if NUM1 != NUM2 and NUM1 != NUM3 and NUM2 != NUM3:
    if NUM1 > NUM2 and NUM1 > NUM3:
        print(NUM1, "Es el mayor")
    else:
        if NUM2 > NUM1 and NUM2 > NUM3:
            print(NUM2, "Es el mayor")
        else:
            print(NUM3, "Es el mayor")

print("La misma pero simplificada:")
if NUM1 != NUM2 and NUM1 != NUM3 and NUM2 != NUM3:
    if NUM1 > NUM2 and NUM1 > NUM3:
        print(NUM1, "Es el mayor")
    elif NUM2 > NUM1 and NUM2 > NUM3:
        print(NUM2, "Es el mayor")
        if:
            print(NUM3, "Es el mayor")
