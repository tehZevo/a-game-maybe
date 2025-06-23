from dataclasses import dataclass

from ..game_command_handler import GameCommandHandler

@dataclass
class JoinRoom:
  room_id: str

class JoinRoomHandler(GameCommandHandler):
  def __init__(self, game):
    super().__init__(JoinRoom, game)

  def handle(self, client_id, command):
    if client_id in self.game.client_room_mapping:
      print(f"[Server] Client {client_id} tried to join room {command.room_id} but was already in a room!")
      return
    if command.room_id not in self.game.rooms:
      print(f"[Server] Client tried to join nonexistent room {command.room_id}!")
      return
    
    self.game.client_room_mapping[client_id] = command.room_id
    room = self.game.rooms[command.room_id]
    self.server.default_channel.send(client_id, E.RoomJoined(room.channel.id))
    room.channel.clients.add(client_id)
    room.on_join(client_id)