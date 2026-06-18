# Pido los segundos
segundos = int(input("Ingrese el número de segundos: "))

# Calculo sus equivalentes en otras medidas de tiempo
equivalente_horas = segundos // 3600
resto = segundos % 3600
equivalente_minutos = resto // 60
resto_segundos = resto % 60

# Imprimo los resultados
print(f"{segundos} segundos equivalen a {equivalente_horas} horas, {equivalente_minutos} minutos y {resto_segundos} segundos.")