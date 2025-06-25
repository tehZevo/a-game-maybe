import time
from dataclasses import dataclass

from game.networking import RoomEventHandler
import game.components as C

@dataclass
class RoomUpdated:
  players: list

class RoomUpdatedHandler(RoomEventHandler):
  def __init__(self, game):
    super().__init__(RoomUpdated, game)

  def handle(self, event):
    print("[Client] Room updated")
    self.game.room.players = set(event.players)
