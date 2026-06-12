numeros = [1,2,3,5,8,13,21]
palabra = "Argentina"

def mayor_de_lista(lista):
    """Te devuelve el mayor número de una lista"""
    mayor = lista[0]
    for valor in lista:
        if valor > mayor:
            mayor = valor
    return mayor

def menor_de_lista(lista):
    """Te devuelve el menor número de una lista"""
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

def contar_letra(palabra, letra):
    """Te devuelve la cantidad de veces que se repite una letra en una palabra"""
    

print(f"El mayor número de la lista es: {mayor_de_lista(numeros)}")
print(f"El menor número de la lista es: {menor_de_lista(numeros)}")
