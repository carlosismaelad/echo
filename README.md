# echo

## Tecnologias usadas
1. Python - A linguagem de programação utilizada para escrever o código do servidor WebSocket e do cliente WebSocket.
2. websockets - Uma biblioteca em Python que fornece suporte para a criação de servidores e clientes WebSocket. 

## Como "rodar" o projeto?
Abra um terminal e rode o arquivo server.py com o comando "python3 server.py"
Em seguida, abra outro terminal e execute o arquivo main.py com o comando "python3 main.py"

## Explicando o que é o projeto
Este é um exemplo simples do funcionamento de um WebSocket.

O servidor HTTP é inicializado na porta 8000 e aguarda por conexões de clientes WebSocket. Quando um cliente WebSocket se conecta, o servidor executa a função handle_websockets para lidar com essa conexão. Essa função é responsável por manipular as mensagens WebSocket recebidas do cliente e enviar respostas de volta para ele.

Enquanto a conexão WebSocket estiver ativa, o servidor aguarda continuamente a recepção de mensagens do cliente usando await websocket.recv(). Quando uma mensagem é recebida, o servidor processa-a conforme você determine e envia uma resposta de volta para o cliente usando await websocket.send(response).

Dessa forma, o servidor WebSocket mantém a conexão ativa com o cliente, permitindo uma comunicação bidirecional em tempo real. Sempre que você envia uma mensagem através do cliente WebSocket, o servidor WebSocket a recebe, processa-a e envia uma resposta de volta para você, como pode ser observado na saída do terminal que você compartilhou.
