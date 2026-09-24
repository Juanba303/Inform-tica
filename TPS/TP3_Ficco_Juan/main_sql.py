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
        #Devuelvo los datos pedidos
        return {"origen": "SQLite", "datos": f"id: {pokemon[0]}", "tiempo_ms": tiempo_ms}
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
        #Freno el cronómetro
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        return {"origen": "PokeAPI", "datos": pokemon, "tiempo_ms": tiempo_ms}