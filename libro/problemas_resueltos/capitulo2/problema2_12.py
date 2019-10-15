SUE = float(input("Introduce el sueldo basico del trabajador: "))
CATE = int(input("Introduce la categoria del trabajador(1-8): "))
HE = int(input("Introduce las horas extras trabajadas: "))
if CATE == 1:
    PHE = 30
elif CATE == 2:
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4:
    PHE = 70
else:
    PHE = 0
if HE > 30:
    NSUE = SUE+30*PHE
else:
    NSUE = SUE+HE*PHE
print(f"El trabajador recibira ${NSUE}")
print("Fin del programa")
