import requests, csv, sqlite3


def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()             
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None  


def pedir_pokemon(nombre):
    try: 
        with open("resumen.csv", "r") as f:
            print(f.read())
            if nombre in f.read():
                print("EL POKEMON YA ESTÁ EN EL ARCHIVO")
            else:
                with open("resumen.csv", "a") as f:
                    print("AGREGANDO")
                    datos = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{nombre}")
                    escritor = csv.writer(f)
                    escritor.writerow([datos["name"], datos["types"][0]["type"]["name"], datos["weight"]]) 
                    print("POKEMON AGREGADO")                   
    except:
        print("CREANDO")
        datos = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{nombre}")
        with open("resumen.csv", "w", newline="") as f:
            campos = ["nombre", "tipo", "peso"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()            
            p = {                
                "nombre": datos["name"], 
                "tipo": datos["types"][0]["type"]["name"], 
                "peso": datos["weight"]
            }
            escritor.writerow(p)
            print("TABLA CREADA Y POKEMON CARGADO")