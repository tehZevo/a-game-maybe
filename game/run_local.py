from threading import Thread

from .client_game import ClientGame
from .server_game import ServerGame
from game.networking import LocalServer, LocalClient

server = LocalServer()
client = LocalClient(server)

def run_server():
    ServerGame(server).run()

Thread(target=run_server, daemon=True).start()

ClientGame(client).run()