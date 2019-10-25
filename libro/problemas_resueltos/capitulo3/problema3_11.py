CAN1 = 0
CAN2 = 0
CAN3 = 0
CAN4 = 0
VOTO = int(input("Introduce el voto: "))
while(VOTO != 0):
    if VOTO == 1:
        CAN1 = CAN1+1
    elif VOTO == 2:
        CAN2 = CAN2+1
    elif VOTO == 3:
        CAN3 = CAN3+1
    elif VOTO == 4:
        CAN4 = CAN4+1
    VOTO = int(input("Introduce el voto: "))
else:
    SUMV = CAN1 + CAN2 + CAN3 + CAN4
    POR1 = (CAN1/SUMV) * 100
    POR2 = (CAN2/SUMV) * 100
    POR3 = (CAN3/SUMV) * 100
    POR4 = (CAN4/SUMV) * 100
print(f"El numero de votos del candidato 1 fue {CAN1} y su porcentaje fue {POR1}")
print(f"El numero de votos del candidato 2 fue {CAN2} y su porcentaje fue {POR2}")
print(f"El numero de votos del candidato 3 fue {CAN3} y su porcentaje fue {POR3}")
print(f"El numero de votos del candidato 4 fue {CAN4} y su porcentaje fue {POR4}")
print(f"La cantidad de votantes fue {SUMV}")

print("Fin del programa")
