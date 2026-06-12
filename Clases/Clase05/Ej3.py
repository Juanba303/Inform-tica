def suma(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación con +, -, /, *: ")

if operacion == '+':
    print(suma(n1,n2))
elif operacion == '-':
    print(restar(n1,n2))
elif operacion == '*':
    print(multiplicar(n1,n2))
elif operacion == '/':
    print(dividir(n1,n2))
