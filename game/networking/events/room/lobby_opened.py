from dataclasses import dataclass

from game.networking import RoomEventHandler

@dataclass
class LobbyOpened:
  pass

class LobbyOpenedHandler(RoomEventHandler):
  def __init__(self, game):
    super().__init__(LobbyOpened, game)

  def handle(self, event):
    print("[Client] Lobby opened, sending ready!")
    self.game.room_channel.send(E.PlayerReady())