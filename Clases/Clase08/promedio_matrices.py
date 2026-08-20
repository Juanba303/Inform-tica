notas = [[8, 7, 9],
        [5, 6, 7],
        [10, 9, 8]]
nombres = ["Ana", "Beto", "Caro"]

for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    estado = "APROBÓ" if promedio >= 6 else "RECUPERA"
    print(f"{nombres[i]}: {promedio:.2f} -> {estado}")