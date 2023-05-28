from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

#levantar server uvicorn main:app --reload

class Jugador(BaseModel):
    id: int
    nombre: str
    raza: str
    rol: str
    rutaFoto: str
    hp: int
    mana: int
    xp:int
    nivel:int
    
jugadores_list = [Jugador(id=1,nombre="Gimli",raza="Enano",rol="Tanque",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=2,nombre="Aragorn",raza="Humano",rol="Luchador",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=3,nombre="Legolas",raza="Elfo",rol="Ranger",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=4,nombre="Gandalf",raza="Istari",rol="Mago",rutaFoto="",hp=18,mana=15,xp=12,nivel=8)]

@app.get("/players")
async def root():
    return "Hola FastAPI, estamos desplegados en casita, en la parte de jugadores"

@app.get("/playerslist")
async def userlist():
    return jugadores_list

@app.get("/player/{id}")
async def player(id: int):
    players = filter(lambda player: player.id == id, jugadores_list)
    return list(players)[0]