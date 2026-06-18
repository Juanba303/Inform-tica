# Pido la edad
edad = int(input("Ingrese su edad: "))

# Calculo los equivalentes y latidos del corazón aproximados
dias = edad * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
latidos = minutos * 70

# Imprimo los resultados
print(f"En {edad} años aproximadamente viviste: \n\t Días: {dias} \n\t Horas: {horas} \n\t Minutos: {minutos} \n\t Segundos: {segundos} \n\t Tu corazón latió aproximadamente: {latidos} veces")