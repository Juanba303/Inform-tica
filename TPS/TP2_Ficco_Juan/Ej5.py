productos = []
subtotal = 0
descuento = 0
club = str(input("¿Sos cliente CLUB? (S/N): "))
while club != "S" and club != "N":
    club = str(input("Ingrese un valor válido (S/N):"))

def cargar_productos():
    productos = []
    while True:
        producto = str(input("Ingrese producto ('fin' para terminar): "))
        if producto == "fin":
            break
        precio = float(input("Ingrese el precio: "))
        productos.append([producto,precio])
    return productos

def calcular_subtotal(productos):
    subtotal = 0
    for producto in productos:
        subtotal += producto[1]
    return subtotal

def calcular_descuento(subtotal, cantidad_productos, es_club):
    descuento = 0

    if subtotal > 50000:
        descuento = subtotal * 0.15
    elif subtotal > 20000:
        descuento = subtotal * 0.10
    elif subtotal > 10000:
        descuento = subtotal * 0.05    

    if cantidad_productos > 5:
        descuento += 1000

    if es_club == "S":
        descuento += (subtotal - descuento) * 0.05

    return descuento

# Agregué 'es_club' como argumento porque sino no iba a poder mostrar el descuento del club
def mostrar_resumen(productos, subtotal, descuento, total, es_club):
    print("\n=== RESUMEN ===\nLista de productos:")
    for producto in productos:
        print(f"Nombre: {producto[0]}   -   Precio: ${producto[1]}")
    print(f"Subtotal: ${subtotal}")

    if subtotal > 50000:
        print(f"Descuento por subtotal > $50000 (15%): -${subtotal * 0.15}")
    elif subtotal > 20000:
        print(f"Descuento por subtotal > $20000 (10%): -${subtotal * 0.10}")
    elif subtotal > 10000:
        print(f"Descuento por subtotal > $10000 (5%): -${subtotal * 0.05}")

    if len(productos) > 5:
        print(f"Descuento por cantidad de productos > 5: -$1000")

    if es_club == "S":
        print(f"Descuento por club: -5%")

    return f"{subtotal} - {descuento} = {total}"


productos = cargar_productos()
subtotal = calcular_subtotal(productos)
descuento = calcular_descuento(subtotal,len(productos),club)
total = subtotal - descuento
print(mostrar_resumen(productos, subtotal, descuento, total, club))