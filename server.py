import asyncio
import websockets

async def handle_websockets(websocket, path):
    # Lógicas para manipular as mensagens websocket

    while True:
        message = await websocket.recv()
        # Lógica para processar a mensagem recebida
        # Exemplo: enviar uma resposta

        response = f"Recebi a mensagem: {message}"

        await websocket.send(response)

async def start_server():
    server = await websockets.serve(handle_websockets, 'localhost', 8000)
    print("Servidor websocket iniciado")
    await server.wait_closed()

asyncio.run(start_server())