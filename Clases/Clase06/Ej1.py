temperaturas = [29,5,32]

def temperatura_promedio(temps):
    """Te devuelve la temperatura promedio"""
    promedio = 0
    for temp in temps:
        promedio += temp
    return promedio / len(temps)

def dias_calurosos(temps, limite=30):
    """Te devuelve las temperaturas que superan el límite"""
    supera = []
    for temp in temps:
        if temp > limite:
            supera.append(temp)
    return supera

def clasificar_dia(temp):
    """Te devuelve la flasificación de la temperatura"""
    if temp < 20:
        return "Frío"
    elif temp >= 20 and temp < 30:
        return "Templado"
    elif temp >= 30:
        return "Caluroso"

print(temperatura_promedio(temperaturas))
print(dias_calurosos(temperaturas))
print(clasificar_dia(temperaturas[0]))
