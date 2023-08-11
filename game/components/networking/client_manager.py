from game.ecs import Component
from game.networking import Client
from game.networking.commands.test_command import TestCommand
from game.networking.events import TilesetUpdatedHandler, ActorSpawnedHandler, PositionUpdatedHandler

class TestConnectHandler:
  def handle_connect(self, client):
    client.send(TestCommand("HELLO WORLD!"))

class ClientManager(Component):
  def __init__(self):
    super().__init__()

  def start(self):
    self.client = Client(
      connect_handlers=[TestConnectHandler()],
      event_handlers=[
        TilesetUpdatedHandler(self),
        ActorSpawnedHandler(self),
        PositionUpdatedHandler(self),
      ]
    )
    self.client.connect()
