numero = 303
respuesta = 0
intentos = 0

while True:
    respuesta = int(input("Ingresá un número: "))

    if respuesta > numero:
        print("Es más chico")
        intentos += 1
    elif respuesta < numero:
        print("Es más grande")
        intentos += 1
    else:
        print(f"¡Adivinaste! Te tomó {intentos} intentos")
        break