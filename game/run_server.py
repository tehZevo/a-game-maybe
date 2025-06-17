from .server_game import ServerGame
from game.networking import WebsocketServer

HOST = "localhost"
PORT = 8765

server = WebsocketServer(HOST, PORT)
the_game = ServerGame(server)
the_game.run()
