#Importé esta librería para que pi ya esté definido y no tenga que escribirlo yo
import math

#Pido el radio del círculo
radio = float(input("Radio del círculo: "))

#Calculo el área y el perímetro
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

#Imprimo los resultados
print(f"Para un círculo de radio {radio:.2f}:")
print(f"Área: {area:.2f} unidades²")
print(f"Perímetro: {perimetro:.2f} unidades")