alumnos = [
    ["Ana Lopez", 8, 7, None],
    ["Pedro Gomez", 4, 6, 7],
    ["Lucia Perez", 9, 9, None],
    ["Juan Diaz", 3, 5, 4],
]

promocion = 0
regular = 0
libre = 0
promedio_clase = 0
mejor_alumno = [0,0]
peor_alumno = [0,11]

print("-"*72)
print(f"{"INFORME DE NOTAS":>44}")
print("-"*72)
print(f"{"Nombre":<23}|{"Promedio":<23}|{"Estado:":<23}")
print("-"*72)
for alumno in alumnos:
    print(f"{alumno[0]:<23}|",end="")

    if alumno[3] == None:
        promedio = (alumno[1] + alumno[2]) / 2
    else:
        promedio = (alumno[1] + alumno[2] + alumno[3]) / 3

    promedio_clase += promedio
    if promedio > mejor_alumno[1]:
        mejor_alumno = [alumno[0], promedio]
    print(f"{promedio:<23.2f}|",end="")

    if promedio < peor_alumno[1]:
        peor_alumno = [alumno[0], promedio]

    if promedio < 6:
        libre += 1
        print(f"{"Libre":<23}")
    elif promedio < 8:
        regular += 1
        print(f"{"Regular":<23}")
    else:
        promocion += 1
        print(f"{"Promociona":<23}")


promedio_clase = promedio_clase / len(alumnos)
print("-"*72)
print(f"{"Promocionados":<23}: {promocion:<23}")
print(f"{"Regulares":<23}: {regular:<23}")
print(f"{"Libres":<23}: {libre:<23}")
print(f"{"Promedio del curso:":<23}: {promedio_clase:<23.2f}")
print(f"{"Mejor alumno:":<23}: {mejor_alumno[0]} ({mejor_alumno[1]})")
print(f"{"Peor alumno:":<23}: {peor_alumno[0]} ({peor_alumno[1]})")