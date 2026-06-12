def area_rectangulo(base, altura):
    if base > 0 and altura > 0:
        return base * altura
    else:
        return "Los valores deben ser mayores a 0"

print(area_rectangulo(5,3))
print(area_rectangulo(10,2))