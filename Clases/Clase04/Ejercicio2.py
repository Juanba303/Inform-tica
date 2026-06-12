notas = []
n_notas = int(input("Ingrese su cantidad de notas: "))
promedio_aux = 0
promedio = 0

for i in range(n_notas):
    notas.append(int(input("Ingrese nota: ")))
    promedio_aux += notas[i]
promedio = promedio_aux / n_notas

print(f"- Lista completa: {notas}\n- Promedio: {promedio:.2f}\n- Nota más alta: {max(notas)}\n- Nota más baja: {min(notas)}")

while True:
    continuar = input("Querés agregar otra nota? Ingrese S/N: ") == "S"
    if continuar:
        notas.append(int(input("Ingrese nota: ")))
        promedio_aux += notas[-1]
        n_notas += 1
    else:
        print(f"- Lista completa: {notas}\n- Promedio: {promedio:.2f}\n- Nota más alta: {max(notas)}\n- Nota más baja: {min(notas)}")
        break
    promedio = promedio_aux / n_notas
    print(f"- Lista completa: {notas}\n- Promedio: {promedio:.2f}\n- Nota más alta: {max(notas)}\n- Nota más baja: {min(notas)}")

