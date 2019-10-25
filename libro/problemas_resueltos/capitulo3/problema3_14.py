AP1 = 0
AP2 = 0
AP3 = 0
AP4 = 0
AP5 = 0
RECAU = 0
P1 = float(input("Introduce el precio que hay en la localidad 1: "))
P2 = float(input("Introduce el precio que hay en la localidad 2: "))
P3 = float(input("Introduce el precio que hay en la localidad 3: "))
P4 = float(input("Introduce el precio que hay en la localidad 4: "))
P5 = float(input("Introduce el precio que hay en la localidad 5: "))
CLAVE = int(input("Introduce la clave de la localidad: "))
CANT = int(input("Introduce la cantidad de boletos vendidos: "))

while(CLAVE != (-1) and CANT != (-1)):
    if CLAVE == 1:
        PRE = P1*CANT
        AP1 = AP1+CANT
    elif CLAVE == 2:
        PRE = P2*CANT
        AP2 = AP2+CANT
    elif CLAVE == 3:
        PRE = P3*CANT
        AP3 = AP3+CANT
    elif CLAVE == 4:
        PRE = P4*CANT
        AP4 = AP4+CANT
    elif CLAVE == 5:
        PRE = P5*CANT
        AP5 = AP5+CANT
    print(f"La clave de la localidad es {CLAVE}, la cantidad de boletos vendidos en esa localidad es {CANT} y el total vendido es ${PRE}")
    RECAU = RECAU + PRE
    CLAVE = int(input("Introduce la clave de la localidad: "))
    CANT = int(input("Introduce la cantidad de boletos vendidos: "))
else:
    print(f"Los boletos vendidos tipo 1 son {AP1}")
    print(f"Los boletos vendidos tipo 2 son {AP2}")
    print(f"Los boletos vendidos tipo 3 son {AP3}")
    print(f"Los boletos vendidos tipo 4 son {AP4}")
    print(f"Los boletos vendidos tipo 5 son {AP5}")
    print(f"La recaudacion total del estadio es ${RECAU}")
print("Fin del programa")
