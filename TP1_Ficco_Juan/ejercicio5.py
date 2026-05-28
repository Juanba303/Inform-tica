#Importo math para hacer la raíz cuadrada más fácilmente
import math

#Defino las coordenadas de los puntos
x1 = int(input("Ingrese el x del primer punto: "))
y1 = int(input("Ingrese el y del primer punto: "))
x2 = int(input("Ingrese el x del segundo punto: "))
y2 = int(input("Ingrese el y del segundo punto: "))

#Calculo la distancia
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#Imprimo los resultados
print(f"Distancia entre ({x1}, {y1}) y ({x2}, {y2}): {distancia:.1f}")