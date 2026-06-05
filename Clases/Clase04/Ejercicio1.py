notas = [9,8,7,8,9,10,5]
suma = 0
aprobados = 0
desaprobados = 0

for nota in notas:
    suma += nota

    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"- La suma de notas es de: {suma}\n- Hubieron {aprobados} aprobados\n- Hubieron {desaprobados} desaprobados")