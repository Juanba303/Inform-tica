import requests

def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()             
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None                 
        

url = "https://pokeapi.co/api/v2/pokemon/pikachu" 
datos = consultar_api(url)

if datos is not None:
    print(datos["name"], "pesa", datos["weight"])