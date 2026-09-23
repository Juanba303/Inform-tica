#Primero importo todo
from fastapi import FastAPI, HTTPException
import csv
import requests
import time

#Uso la consulta que nos dio el profe 
def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()             
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None                 

#Defino la app
app = FastAPI()

#Programo la consulta del usuario por un pokemon según su nombre o ID
@app.get("/pokemon/{clave}")
def consultar_pokemon(clave: str):
    #Inicio el cronómetro
    inicio = time.perf_counter()
    #Primero compruebo si el pokemon existe el archivo csv con un try para que no tenga errores
    try:
        #Leo el archivo
        with open("pokemones.csv", "r") as f:
            lector = csv.DictReader(f)
            #Reviso fila por fila para ver si el pokemon ya estaba en el archivo
            for fila in lector:
                #Revisa si el pokemon está en el archivo comparando con su nombre o ID
                if fila["nombre"] == clave or fila["id"] == clave:
                    #Finalizo el cronómetro y calculo el tiempo de ejecución
                    fin = time.perf_counter()
                    tiempo_ms = (fin - inicio) * 1000
                    #Devuelvo los datos pedidos
                    return {"origen": "csv", "datos": fila, "tiempo_ms": tiempo_ms}              
        #Este es el caso en el que el pokemon no esté en el archivo
        #Los agrego en el archivo
        with open("pokemones.csv", "a") as f:
            #Asigno una variable para los datos
            datos = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{clave}")
            if datos is None:
                raise HTTPException(status_code=404, detail="El Pokemon buscado no existe")
            escritor = csv.writer(f)
            escritor.writerow([
                datos["id"], 
                datos["name"], 
                datos["types"][0]["type"]["name"], 
                datos["height"], 
                datos["weight"], 
                datos["base_experience"], 
                datos["stats"][0]["base_stat"], 
                datos["stats"][1]["base_stat"], 
                datos["stats"][2]["base_stat"], 
                datos["stats"][5]["base_stat"]
            ])
        #Finalizo el cronómetro y calculo el tiempo de ejecución
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        #Devuelvo los datos pedidos
        return {"origen": "PokeAPI", "datos": {
                "id": datos["id"],
                "name": datos["name"],
                "type": datos["types"][0]["type"]["name"],
                "height": datos["height"],
                "weight": datos["weight"],
                "base_experience": datos["base_experience"],
                "hp": datos["stats"][0]["base_stat"],
                "attack": datos["stats"][1]["base_stat"],
                "defense": datos["stats"][2]["base_stat"],
                "speed": datos["stats"][5]["base_stat"]
            }, "tiempo_ms": tiempo_ms}
    #Este es el caso en donde el archivo no está creado
    except FileNotFoundError:
        #Defino los campos
        campos = ["id", "nombre", "tipo", "altura", "peso", "experiencia base", "hp", "ataque", "defensa", "velocidad"]
        #Se crea el archivo
        with open("pokemones.csv", "w") as f:
            #Asigno una variable para los datos
            datos = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{clave}")
            escritor = csv.DictWriter(f, fieldnames=campos)
            #Se escribe el cabezal
            escritor.writeheader()
            #Se escriben los datos de los pokemones fila por fila
            escritor.writerow({
                "id": datos["id"],
                "nombre": datos["name"],
                "tipo": datos["types"][0]["type"]["name"],
                "altura": datos["height"],
                "peso": datos["weight"],
                "experiencia base": datos["base_experience"],
                "hp": datos["stats"][0]["base_stat"],
                "ataque": datos["stats"][1]["base_stat"],
                "defensa": datos["stats"][2]["base_stat"],
                "velocidad": datos["stats"][5]["base_stat"]
            })
            #Finalizo el cronómetro y calculo el tiempo de ejecución
            fin = time.perf_counter()
            tiempo_ms = (fin - inicio) * 1000
            #Devuelvo los datos pedidos
            return {
            "origen": "PokeAPI", 
            "datos": {
                "id": datos["id"],
                "name": datos["name"],
                "type": datos["types"][0]["type"]["name"],
                "height": datos["height"],
                "weight": datos["weight"],
                "base_experience": datos["base_experience"]
            }, "tiempo_ms": tiempo_ms}