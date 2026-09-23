#Importo todo
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

con = sqlite3.connect("pokemones.db")
cur = con.cursor()

cur.execute()