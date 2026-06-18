frase = "Hola tonto aburrido como estas"
lista_negra = ["tonto", "aburrido", "tarado"]
frase_split = frase.split()
frase_censurada = ""

print(frase_split)

for palabra in frase_split:
    if palabra in lista_negra:
        frase_censurada += "*"*len(palabra) + ' '
    else:
        frase_censurada += palabra + ' '

print(frase)
print(frase_censurada)