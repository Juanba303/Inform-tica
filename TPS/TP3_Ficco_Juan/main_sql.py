#Importo todo
from fastapi import FastAPI, HTTPException
import sqlite3
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

    #Me conecto a la tabla
    con = sqlite3.connect("pokemones.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS pokemones"
        "(id INTEGER, nombre TEXT, tipo TEXT, altura FLOAT, peso FLOAT, experiencia_base INTEGER, hp INTEGER, ataque INTEGER, defensa INTEGER, velocidad INTEGER)")
    #Busco el pokemon en la tabla
    cur.execute("SELECT * FROM pokemones WHERE nombre = ? or id = ?",
                (clave.lower(), clave))
    pokemon = cur.fetchone()
    #Este es el caso en donde el pokemon sí está en la tabla
    if pokemon != None:
        #Freno el cronómetro
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        #Defino los datos para después retornarlos como diccionario porque sino retorna todo sin clasificación
        datos_pokemon = {
        "id": pokemon[0],
        "nombre": pokemon[1],
        "tipo": pokemon[2],
        "altura": pokemon[3],
        "peso": pokemon[4],
        "experiencia_base": pokemon[5],
        "hp": pokemon[6],
        "ataque": pokemon[7],
        "defensa": pokemon[8],
        "velocidad": pokemon[9],
        }
        #Devuelvo los datos pedidos
        return {"origen": "SQLite", "datos": datos_pokemon, "tiempo_ms": tiempo_ms}
    #Si no está en la tabla
    else:
        #Asigno una variable a los datos
        datos = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{clave}")
        #Si el pokemon no existe, retorna un mensaje de error
        if datos is None:
            raise HTTPException(status_code=404, detail="El Pokemon buscado no existe")
        #Inserto los valores a la tabla
        cur.execute("INSERT INTO pokemones VALUES (?,?,?,?,?,?,?,?,?,?)", (datos["id"], 
                                                                       datos["name"], 
                                                                       datos["types"][0]["type"]["name"], 
                                                                       datos["height"],
                                                                       datos["weight"],
                                                                       datos["base_experience"],
                                                                       datos["stats"][0]["base_stat"],
                                                                       datos["stats"][1]["base_stat"],
                                                                       datos["stats"][2]["base_stat"],
                                                                       datos["stats"][5]["base_stat"]))
        con.commit()
        cur.execute("SELECT * FROM pokemones WHERE nombre = ? or id = ?",
            (clave.lower(), clave))
        pokemon = cur.fetchone()
        datos_pokemon = {
        "id": pokemon[0],
        "nombre": pokemon[1],
        "tipo": pokemon[2],
        "altura": pokemon[3],
        "peso": pokemon[4],
        "experiencia_base": pokemon[5],
        "hp": pokemon[6],
        "ataque": pokemon[7],
        "defensa": pokemon[8],
        "velocidad": pokemon[9],
        }
        #Freno el cronómetro
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        return {"origen": "PokeAPI", "datos": datos_pokemon, "tiempo_ms": tiempo_ms}