#Se definen las listas "frase", "frase_censurada" y "lista_negra" con las palabras a censurar
frase = "Hola tonto aburrido como estas"
lista_negra = ["tonto", "aburrido", "tarado"]
frase_censurada = ""

#Se define "frase_split" para tener una lista con todas las palabras de la frase
frase_split = frase.split()
print(frase_split)

#Para cada palabra en el split de la frase:
for palabra in frase_split:
    #Si la palabra está en lista_negra:
    if palabra in lista_negra:
        #Se concatenan tantos "*" según la cantidad de letras de la palabra 
        frase_censurada += "*"*len(palabra) + ' '
    else:
        #Simplemente se concatena la palabra con un espacio para que quede legible
        frase_censurada += palabra + ' '

#Se prueban las funciones
print(f"La frase original es: {frase}")
print(f"La frase censurada es: {frase_censurada}")