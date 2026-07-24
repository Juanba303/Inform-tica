n_notas = 0
notas = []

def promedio(notas):
    return sum(notas) / len(notas)

def mas_alta(notas):
    mayor = notas[0]
    for nota in notas:
        if nota > mayor:
            mayor = nota
    return mayor

def mas_baja(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor

def contar_aprobados(notas):
    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
    return aprobados

def distribucion(notas):
    reprobados_graves = 0
    reprobados = 0
    regulares = 0

while n_notas <= 0:
    n_notas = int(input("Ingrese la cantidad de notas (número positivo): "))

for i in range(n_notas):
    notas.append(int(input(f"Ingrese nota {i+1} (1-10): ")))
    while notas[i] < 1 or notas[i] > 10:
        notas.pop(i)
        notas.append(int(input(f"Nota inválida, ingrese nota {i+1} (1-10): ")))

print(f"=== ANÁLISIS ===\nNotas: {notas}\nPromedio: {promedio(notas):.2}\nMás alta: {mas_alta(notas)}\nMás baja: {mas_baja(notas)}\nAprobados: {contar_aprobados(notas)} de {len(notas)} ({contar_aprobados(notas) / len(notas):.0%})\nDistribución: ")