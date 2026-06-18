import random

def cargar_jugador(numero):
        carac = []
        suma = 0
        carac.append(int(input("Ingrese la FUERZA: ")))
        while carac[0] > 10:
                carac.pop(0)
                carac.append(int(input("La suma de tus características no puede sumar más de 10, ingrese otro valor: ")))
        suma += carac[0]
        carac.append(int(input("Ingrese la VELOCIDAD: ")))
        while suma + carac[1] > 10:
                carac.pop(1)
                carac.append(int(input("La suma de tus características no puede sumar más de 10, ingrese otro valor: ")))
        suma += carac[1]
        carac.append(int(input("Ingrese el PODER: ")))
        while suma + carac[2] > 10:
                carac.pop(2)
                carac.append(int(input("La suma de tus características no puede sumar más ni menos de 10, ingrese otro valor: ")))
        suma += carac[2]
        return carac

def calcular_daño(atacante):
        daño = 0

jugador1 = cargar_jugador(1)
print(f"\nJUGADOR 1:\n\t- FUERZA: {jugador1[0]}\n\t- VELOCIDAD: {jugador1[1]}\n\t- PODER: {jugador1[2]}\n")

jugador2 = cargar_jugador(2)
print(f"\nJUGADOR 2:\n\t- FUERZA: {jugador2[0]}\n\t- VELOCIDAD: {jugador2[1]}\n\t- PODER: {jugador2[2]}\n")