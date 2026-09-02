import requests

def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()             
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None                 

peso_promedio = 0
nombres = ["charmeleon", "squirtle", "charmander", "jigglypuff", "alakazam"]
pokemones = []
for nombre in nombres:
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}" 
    datos = consultar_api(url)
    if datos is not None:
        pokemones.append(datos)

resumen = []
for p in pokemones:
    resumen.append({
        "nombre": p["name"],
        "tipo":   p["types"][0]["type"]["name"],
        "peso":   p["weight"],
    })

print(f"{'NOMBRE':<12}{'TIPO':<10}{'PESO(kg)':>9}")
print("-" * 31)
for p in resumen:
    print(f"{p['nombre']:<12}{p['tipo']:<10}{p['peso']/10:>9.1f}")
    peso_promedio += p["peso"]/10

print("\nSolo los tipo fuego:")
for p in resumen:
    if p["tipo"] == "fire":
        print(p["nombre"])

print(f"Peso promedio: {peso_promedio / len(pokemones)}")