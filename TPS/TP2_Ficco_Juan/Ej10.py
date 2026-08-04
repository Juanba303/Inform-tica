menu = 0

def cifrar(texto, n):
    texto_resultado = []
    for letra in texto:
        if letra.isupper():
            codigo = ord(letra) - ord("A")
            nuevo_codigo = ((codigo + n) % 26) + (ord("A"))
            texto_resultado.append(chr(nuevo_codigo))
        elif letra.islower():
            codigo = ord(letra) - ord("a")
            nuevo_codigo = (codigo + n) % 26 + (ord("a"))
            texto_resultado.append(chr(nuevo_codigo))
        else:
            texto_resultado.append(letra)
    print("Texto cifrado:")
    for letra in texto_resultado:
        print(letra, end="")

def descifrar(texto, n):
    texto_resultado = []
    for letra in texto:
        if letra.isupper():
            codigo = ord(letra) - ord("A")
            nuevo_codigo = ((codigo - n) % 26) + (ord("A"))
            texto_resultado.append(chr(nuevo_codigo))
        elif letra.islower():
            codigo = ord(letra) - ord("a")
            nuevo_codigo = (codigo - n) % 26 + (ord("a"))
            texto_resultado.append(chr(nuevo_codigo))
        else:
            texto_resultado.append(letra)
    print("Texto descifrado:")
    for letra in texto_resultado:
        print(letra, end="")

while menu == 0:
    print("1- Cifrar código")
    print("2- Descifrar código")

    menu = int(input("Ingrese opción: "))
    while menu > 2 or menu < 1:
        menu = int(input("Ingrese opción válida: "))

if menu == 1:
    cifrar(str(input("Ingrese su texto a cifrar: ")), int(input("Ingrese su número de desplazamiento: ")))
    print("")

if menu == 2:
    descifrar(str(input("Ingrese su texto a descifrar: ")), int(input("Ingrese su número de desplazamiento: ")))
    print("")