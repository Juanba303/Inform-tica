from fastapi import FastAPI, Header, HTTPException
from datos import pokemones
import os

app = FastAPI()

@app.get("/pokemones")
def listar(tipo: str = None):
    if tipo is None:
        return pokemones
    return [ f"El tipo es:{p['tipo']}" for p in pokemones if p["tipo"] == tipo]


@app.get("/pokemones/{nombre}")
def obtener(nombre: str):
    for p in pokemones:
        if p["nombre"] == nombre.lower() or p["id"] == nombre:
            return p
    raise HTTPException(status_code=404,
                        detail="Pokémon no encontrado")

@app.get("/stats")
def estadisticas():
    total = len(pokemones)
    peso_prom = sum(p["peso"] for p in pokemones) / total
    return {"cantidad": total,
            "peso_promedio_kg": round(peso_prom / 10, 2)}

@app.get("/privado")
def privado(x_api_key: str = Header(None)):
    if x_api_key != os.environ.get("API_KEY"):
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"secreto": "datos protegidos"}
