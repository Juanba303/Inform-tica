biblioteca = [["El Aleph", "Borges", 1949, False],["Cien años de soledad", "García Márquez", 1967, True],["Ficciones", "Borges", 1944, False],["Rayuela", "Cortázar", 1963, True],["1984", "Orwell", 1949, False]]
menu = 0

def mostrar_menu():
    print("=== BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Listar todos los libros")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Listar solo disponibles")
    print("7. Listar solo prestados")
    print("8. Estadísticas")
    print("9. Salir\n")
    
    menu = int(input("Elegir opción: "))
    while menu < 1 or menu > 9:
        menu = int(input("Ingrese valor válido (1-9): "))
    return menu

def agregar_libro(biblioteca, titulo, autor, año):
    biblioteca.append([titulo, autor, año, False])

def listar_libros(biblioteca):
    for libro in biblioteca:
        print(f"Nombre: {libro[0]}\nAutor: {libro[1]}\nAño de publicación: {libro[2]}\nPrestado: {libro[3]}\n")

def buscar_libro(biblioteca, texto):
    for libro in biblioteca:
        if texto.lower() in libro[0].lower():
            print(f"Nombre: {libro[0]}\nAutor: {libro[1]}\nAño de publicación: {libro[2]}\nPrestado: {libro[3]}\n")

def prestar(biblioteca, titulo):
    for libro in biblioteca:
        if titulo.lower() == libro[0].lower():
            if libro[3] == False:
                libro[3] = True
                return True
            else:
                return False
    return False

def devolver(biblioteca, titulo):
    for libro in biblioteca:
        if titulo.lower() == libro[0].lower():
            if libro[3]:
                libro[3] = False
                return True
            else:
                return False
    return False

def disponibles(biblioteca):
    for libro in biblioteca:
        if libro[3] == False:
            print(f"Nombre: {libro[0]}\nAutor: {libro[1]}\nAño de publicación: {libro[2]}\nPrestado: {libro[3]}\n")

def prestados(biblioteca):
    for libro in biblioteca:
        if libro[3]:
            print(f"Nombre: {libro[0]}\nAutor: {libro[1]}\nAño de publicación: {libro[2]}\nPrestado: {libro[3]}\n")

def estadisticas(biblioteca):
    prestados = 0
    for libro in biblioteca:
        if libro[3]:
            prestados += 1
    return f"Libros: {len(biblioteca)}\nLibros prestados: {prestados}"


while menu != 9:
    menu = mostrar_menu()

    if menu == 1:
        print("=== AGREGAR UN LIBRO ===")
        agregar_libro(biblioteca, str(input("Nombre del libro: ")), str(input("Autor: ")), int(input("Año de publicación: ")))

    if menu == 2:
        print("=== LISTA DE LIBROS ===")
        listar_libros(biblioteca)

    if menu == 3:
        print("=== BÚSQUEDA DE LIBROS ===")
        buscar_libro(biblioteca, str(input("Ingrese su búsqueda: ")))

    if menu == 4:
        print("=== PRESTAR LIBRO ===")
        if prestar(biblioteca, str(input("Ingrese el libro a prestar: "))):
            print("Éxito")
        else:
            print("El libro no se encontró o ya está prestado")

    if menu == 5:
        print("=== DEVOLVER LIBRO ===")
        if devolver(biblioteca, str(input("Ingrese el libro a devolver: "))):
            print("Éxito")
        else:
            print("El libro no se encontró o no estaba prestado")

    if menu == 6:
        print("=== LIBROS DISPONIBLES ===")
        disponibles(biblioteca)

    if menu == 7:
        print("=== LIBROS PRESTADOS ===")
        prestados(biblioteca)

    if menu == 8:
        print("=== ESTADÍSTICAS ===")
        print(estadisticas(biblioteca))

print("Saliste de la biblioteca")