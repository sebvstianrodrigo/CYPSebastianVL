PRI = 0
SEG = 1
for i in range(3, 180, 1):
    SIG = PRI + SEG
    PRI = SEG
    SEG = SIG
else: 
    print(f"El termino 180 de la secuencia FIBONACCI es {SIG}")

print("Fin del programa")
