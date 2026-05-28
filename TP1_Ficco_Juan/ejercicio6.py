#Pido los datos de la cuenta
monto_cuenta = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que quiere dejar: "))
personas = int(input("Ingrese el número de personas que van a pagar la cuenta: "))

#Calculo la propina, el monto total a pagar y el monto por persona
propina = monto_cuenta * porcentaje_propina / 100
monto_total = monto_cuenta + propina
por_persona = monto_total / personas

#Imprimo el resumen
print("Resumen:")
print(f"\t Cuenta: ${monto_cuenta:.2f}")
print(f"\t Propina: ${propina:.2f}")
print(f"\t Total a pagar: ${monto_total:.2f}")
print(f"\t Por persona: ${por_persona:.2f}")