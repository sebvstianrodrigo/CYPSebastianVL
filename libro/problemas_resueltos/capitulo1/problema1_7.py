L1 = float(input("Introduce el primer lado del triangulo:"))
L2 = float(input("Introduce el segundo lado del triangulo:"))
L3 = float(input("Introduce el tercer lado del triangulo:"))
S = (L1 + L2 + L3) / 2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print(f"El area del triangulo es {AREA}")
