import random

palabras = ["PALINDROMO", "CORTINA", "PARAGUAS", "CONDUCTISMO", "RESULTADO", "RETROALIMENTACION", "BUSCAMINAS", "AVIONETA", "COMPUTACION", "TELEFONO"]

palabra = list(random.choice(palabras))
palabra_revelada = list("_"*len(palabra))
letras_usadas = []
letra_pedida = ""
vidas = 6

for letra in palabra_revelada:
    print(f"{letra} ",end="")
print("")
print(f"Tenés {vidas} vidas disponibles")

while palabra_revelada != palabra and vidas > 0:
    letra_pedida = str(input("Ingrese una letra: ")).upper()
    while len(letra_pedida) != 1 or not letra_pedida.isupper() and not letra_pedida.islower():
        letra_pedida = str(input("Ingrese una letra válida: ")).upper()

    if letra_pedida not in letras_usadas:
        letras_usadas.append(letra_pedida)
        if letra_pedida in palabra and letra_pedida not in palabra_revelada:
                for i in range(len(palabra)):
                    if letra_pedida == palabra[i]:
                        palabra_revelada.pop(i)
                        palabra_revelada.insert(i,palabra[i])
        else:
            vidas -= 1
    else:
        vidas -= 1


    print("\nPalabra:")
    for letra in palabra_revelada:
        print(f"{letra} ",end="")
    print("")

    print("Letras usadas:")
    for letra in letras_usadas:
        print(f"{letra} ",end="")

    if palabra_revelada != palabra:
        print(f"\nTenés {vidas} vidas disponibles")

    if vidas == 5:
        print("Estado:")
        print("   O")
    elif vidas == 4:
        print("Estado:")
        print("   O")
        print("  /")
    elif vidas == 3:
        print("Estado:")
        print("   O")
        print("  /|")
    elif vidas == 2:
        print("Estado:")
        print("   O")
        print("  /|\\")
    elif vidas == 1:
        print("Estado:")
        print("   O")
        print("  /|\\")
        print("  /")


if vidas == 0:
    print("\nPerdiste :(\nLa palabra era:")
    for letra in palabra:
        print(f"{letra} ",end="")
    print("\nEstado:")
    print("   O")
    print("  /|\\")
    print("  /\\")

else:
    print("\nGanaste :)")