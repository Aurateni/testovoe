import json

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket

app = FastAPI()

html = ""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def webs(websocket: WebSocket):
    number = 0
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        number += 1
        mes = json.loads(data)
        mes['number'] = number
        await websocket.send_json(mes)
        print(data)