MAYPRO = 0
N = int(input("Ingresa el numero de fabricas registradas: "))
if N<=100:
    for i in range(0, N, 1):
        FABRICA = int(input("Ingresa la clave de la fabrica: "))
        TOTANU = 0
        J = 1
        for j in range(0, 12, 1):
            MES = float(input("Ingresa la produccion de la fabrica al mes: "))
            TOTANU = TOTANU + MES
            if J == 6 and MES > 3000000:
                print(f"La clave de la fabrica es {FABRICA}")
        else:
            if TOTANU > MAYPRO:
                MAYPRO = TOTANU
                CLAVE = FABRICA
                print(f"La produccion anual de la fabrica {FABRICA} es ${TOTANU}")
    print(f"La fabrica que mas produjo en el año es la {CLAVE} y la produccion fue de ${MAYPRO}")
else:
    print("Error en numero de fabricas")
print("Fin del programa")
