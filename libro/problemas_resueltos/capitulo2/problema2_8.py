COMPRA = float(input("Introduce el monto de la compra: "))
if COMPRA < 500:
    PAGAR = COMPRA
    print(f"El cliente debe pagar ${PAGAR}")
elif COMPRA <= 1000:
    PAGAR = COMPRA-(COMPRA*0.05)
    print(f"El cliente debe pagar ${PAGAR}")
elif COMPRA <= 7000:
    PAGAR = COMPRA-(COMPRA*0.11)
    print(f"El cliente debe pagar ${PAGAR}")
elif COMPRA <= 15000:
    PAGAR = COMPRA-(COMPRA*0.18)
    print(f"El cliente debe pagar ${PAGAR}")
else:
    PAGAR = COMPRA-(COMPRA*0.25)
    print(f"El cliente debe pagar ${PAGAR}")

print("Fin del programa")

