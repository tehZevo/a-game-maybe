import time
from dataclasses import dataclass

from game.networking import GameEventHandler
import game.components as C

@dataclass
class RoomJoined:
  room_channel_id: str
  lobby_channel_id: str

class RoomJoinedHandler(GameEventHandler):
  def __init__(self, game):
    super().__init__(RoomJoined, game)

  def handle(self, event):
    print("[Client] Room joined:", event.room_channel_id, event.lobby_channel_id)
    #delay - pretend you're a user clicking "ready"
    time.sleep(1)
    self.game.setup_room_and_lobby(event.room_channel_id, event.lobby_channel_id)
