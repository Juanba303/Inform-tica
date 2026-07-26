parrafo = str(input("Ingrese un texto: "))
split_parrafo = parrafo.split()
n_vocales = 0
mas_larga = ""
mas_corta = split_parrafo[0]
inversa = " ".join(split_parrafo[::-1])
sin_vocales = ""

for palabra in split_parrafo:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra
    if len(palabra) < len(mas_corta):
        mas_corta = palabra

for letra in parrafo:
    if letra in ["A","E","I","O","U","Á","É","Í","Ó","Ú","a","e","i","o","u","á","é","í","ó","ú"]:
        n_vocales += 1
        sin_vocales += "*"
    else:
        sin_vocales += letra

print(f"\nPalabras: {len(split_parrafo)}\nVocales: {n_vocales}\nMás larga: {mas_larga}\nMás corta: {mas_corta}\nSin vocales: {sin_vocales}\nOrden inverso: {inversa}")