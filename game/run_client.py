from .client_game import ClientGame
from game.networking import WebsocketClient

URL = "ws://localhost:8765"

client = WebsocketClient("ws://localhost:8765")
the_game = ClientGame(client)
the_game.run()
