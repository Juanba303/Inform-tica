#Se piden la base y la altura de un rectángulo
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

#Se calcula el área y el perímetro
area = base * altura
perimetro = 2 * (base + altura)

#Se muestran los resultados
print(f"El área del rectángulo es: {area:.2f} m²")
print(f"El perímetro del rectángulo es: {perimetro:.2f} m")