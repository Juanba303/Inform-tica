def validar_password(pwd):
    tiene_8caracteres = False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    tiene_caracter_especial = False
    problemas = ""

    if len(pwd) >= 8:
        tiene_8caracteres = True
    for c in contrasena:
        if c.isupper():
            tiene_mayuscula = True
        if c.islower():
            tiene_minuscula = True
        if c.isdigit():
            tiene_digito = True
        if c in ["!","@","#","$","%""&","*","?"]:
            tiene_caracter_especial = True

    if tiene_8caracteres == False:
        problemas += "- Debe tener al menos 8 caracteres\n"
    if tiene_mayuscula == False:
        problemas += "- Debe tener al menos un caracter en mayúscula\n"
    if tiene_minuscula == False:
        problemas += "- Debe tener al menos un caracter en minúscula\n"
    if tiene_digito == False:
        problemas += "- Debe tener al menos un dígito (0-9)\n"
    if tiene_caracter_especial == False:
        problemas += "- Debe tener al menos un caracter especial (!@#$%&*?)\n"

    return problemas

contrasena = str(input("Ingrese su contraseña: "))

print(validar_password(contrasena))