P = int(input("Introduce un numero entero: "))
Q = int(input("Introduce otro numero entero: "))
EXP = P**3 + Q**4 - 2*P**2
if EXP < 680:
    print(f"Los valores {P} y {Q} satisfacen la expresion P**3 + Q**4 - 2*P**2 ya que el resultado de esta operacion es {EXP} y es menor a 680")
    print("Fin del programa")
else:
    print(f"Los valores {P} y {Q} no satisfacen la expresion P**3 + Q**4 - 2*P**2 ya que el resultado de esta operacion es {EXP} y es mayor a 680")
    print("Fin del programa")

