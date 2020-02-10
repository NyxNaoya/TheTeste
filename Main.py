import json

from fastapi import FastAPI
from pydantic import BaseModel
from math import sqrt

#Declarada a classe para as variaveis que seriam salvas pelo número
class Item(BaseModel):
    x: int
    y: int


app = FastAPI()

#Esta parte não funciona, não pude prosseguir com ele pois aparece o
#erro {"detail":"Method Not Allowed"}
@app.post("/save/")
async def create_item(item: Item):
    obj = open("save.txt", "w")
    obj = write(item)
    obj = close
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump('save.txt', f, ensure_ascii=False, indent=4)
    return item
    

@app.get("/distancia/")
async def read_user_item(
    x1 : float = 0, y1: float = 0,x2: float = 0, y2: float = 0):
    item = {
        "Abscissa pA": x1, "Ordenada pB": y1, "Abscissa pB": x2,
        "Abscissa do pA": y2
        }
    distAB = sqrt((x1-x2)**2 + ((y1-y2)**2))
    distABres = {"O Valor da distância é": distAB}
    return item, distABres
