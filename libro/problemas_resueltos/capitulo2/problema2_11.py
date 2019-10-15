CLAVE = int(input("Introduce la clave de la zona a la que se llamo: "))
NUMIN = int(input("Introduce el numero de minutos que duro la llamada: "))
if CLAVE == 12:
    COST = NUMIN*2
elif CLAVE == 15:
    COST = NUMIN*2.2
elif CLAVE == 18:
    COST = NUMIN*4.5
elif CLAVE == 19:
    COST = NUMIN*3.5
elif CLAVE == 23:
    COST = NUMIN*6
elif CLAVE == 29:
    COST = NUMIN*5
print(f"El costo total de la llamada es ${COST}")
print("Fin del programa")
