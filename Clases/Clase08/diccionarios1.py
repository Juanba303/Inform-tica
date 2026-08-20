agenda = {
    "Ana": "351-111",
    "Beto": "351-222",
    "Caro": "351-333",
}
menu = 0

def mostrar_menu():
    print("--- MENU ---\n"
          "1- Agregar nuevo contacto\n"
          "2- Buscar contacto\n"
          "3- Lista de contactos\n"
          "4- Salir\n")
    menu = int(input("Elegir opción: "))
    while menu < 1 or menu > 4:
        menu = int(input("Ingrese valor válido (1-4): "))
    return menu

while menu != 4:
    menu = mostrar_menu()

    if menu == 1:
        agenda[input("Nombre del contacto a agregar: ")] = input("Número de teléfono: ")

    if menu == 2:
        nombre = input("Nombre a buscar: ")
        print(f"Número de {nombre}: {agenda.get(nombre, "No se encontró el contacto")}")

    if menu == 3:
        print("--- LISTA DE CONTACTOS ---")
        for nombre, numero in agenda.items():
            print(f"{nombre}: {numero}")
print("Saliste con éxito")