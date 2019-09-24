edad = int( input("Dame tu edad:") )
INE = bool( int( input("Tienes INE (0 No / 1 Si)?:") ) )

if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puede entrar al bar")
else:
    print("Eres menor de edad")
    print("Puedes ir a jugar Lol")
print("Fin del programa")
