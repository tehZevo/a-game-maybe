from dataclasses import dataclass

from ..game_command_handler import GameCommandHandler
import game.networking.events as E

@dataclass
class CreateRoom:
  pass

class CreateRoomHandler(GameCommandHandler):
  def __init__(self, game):
    super().__init__(CreateRoom, game)

  def handle(self, client_id, command):
    #TODO check if client is in other rooms?
    print("[Server] Client requested me to create a room")
    room, room_id = self.game.create_room()
    self.game.client_room_mapping[client_id] = room_id
    lobby_channel_id = room.get_lobby_channel().id
    self.game.server.default_channel.send(client_id, E.RoomJoined(room_id, lobby_channel_id))
    print("[Server] Room", room_id, "created with lobby", lobby_channel_id)
    room.on_join(client_id)