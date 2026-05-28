# Pido los datos
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calulo el IMC y lo imprimo
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc:.2f}")

# Imprimo el tipo de peso según el IMC
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")