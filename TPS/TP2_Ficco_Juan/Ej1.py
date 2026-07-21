def celcius_a_farenheit(c):
    return c * 9/5 + 32

def farenheit_a_celcius(f):
    return (f - 32) * 5/9

def kelvin_a_celcius(k):
    return k - 273.15

def celcius_a_kelvin(c):
    return c + 273.15

temp_final = 0
temp = float(input("Ingrese la temperatura: "))
unidad_origen = str(input("Unidad de origen (C/F/K): "))
unidad_destino = str(input("Unidad de destino (C/F/K): "))

if unidad_origen == "C" and unidad_destino == "F":
    temp_final = celcius_a_farenheit(temp)
elif unidad_origen == "F" and unidad_destino == "C":
    temp_final = farenheit_a_celcius(temp)
elif unidad_origen == "K" and unidad_destino == "C":
    temp_final = kelvin_a_celcius(temp)
elif unidad_origen == "C" and unidad_destino == "K":
    temp_final = celcius_a_kelvin(temp)
elif unidad_origen == "F" and unidad_destino == "K":
    temp_final = celcius_a_kelvin(farenheit_a_celcius(temp))
elif unidad_origen == "K" and unidad_destino == "F":
    temp_final = celcius_a_farenheit(kelvin_a_celcius(temp))

print(f"{temp}{unidad_origen} equivale a {temp_final}{unidad_destino}")