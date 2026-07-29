def tabla_multiplicar(n):
    print(f"Tabla de multiplicar {n}:")
    for i in range(10):
        print(f"{n} x {i+1} = {n*(i+1)}")

def tabla_completa(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(f"{j*i}\t",end="")
        print("\n")

def triangulo(altura):
    for i in range(altura+1):
        print("*"*i)

def triangulo_invertido(altura):
    for i in range(altura+1):
        print("*"*(altura - i))

tabla_multiplicar(4)
tabla_completa(4)
triangulo(30)
triangulo_invertido(30)