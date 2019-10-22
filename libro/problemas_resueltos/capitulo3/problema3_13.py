ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
MES = 0
for i in range(1, 13, 1):
    print(f"Mes { i }:")
    RNO = float(input("Promedio de lluvias del mes Zona Norte:"))
    RCE = float(input("Promedio de lluvias del mes Zona Centro:"))
    RSU = float(input("Promedio de lluvias del mes Zona Sur:"))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
PRORCE = ARCE / 12
print(f"Promedio region centro: {PRORCE}")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif ARCE > ARSU:
    print("La region con mayor lluvia es la region centro")
else:
    print("La region con mayor lluvia es la region sur")

print("Fin del programa")
        

    
