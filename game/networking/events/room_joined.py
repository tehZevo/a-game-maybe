import time
from dataclasses import dataclass

from game.networking import GameEventHandler
import game.components as C

#TODO: pass players here?
@dataclass
class RoomJoined:
  room_channel_id: str
  lobby_channel_id: str
  players: list
  join_code: str

class RoomJoinedHandler(GameEventHandler):
  def __init__(self, game):
    super().__init__(RoomJoined, game)

  def handle(self, event):
    print("[Client] Room joined:", event.join_code)
    self.game.setup_room_and_lobby(event.room_channel_id, event.lobby_channel_id, set(event.players), event.join_code)
