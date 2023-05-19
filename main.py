import asyncio
import websockets

async def connect_websocket():
    async with websockets.connect('ws://localhost:8000') as websocket:

        while True:
            message = input("Digite uma mensagem: ")
            await websocket.send(message)

            response = await websocket.recv()
            print(f"Resposta recebida: {response}")

asyncio.run(connect_websocket())
