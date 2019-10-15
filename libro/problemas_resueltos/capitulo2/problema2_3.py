A = float(input("Introduce el coeficiente A de la ecuacion: "))
B = float(input("Introduce el coeficiente B de la ecuacion: "))
C = float(input("Introduce el coeficiente C de la ecuacion: "))
DIS = B**2 - 4*A*C 
if DIS >= 0:
    X1 = ((-B) + DIS**0.5)/(2*A)
    X2 = ((-B) - DIS**0.5)/(2*A)
    print(f"Las raices reales de la ecuacion son {X1} y {X2}")
    
print("Fin del programa")
