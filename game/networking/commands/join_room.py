from dataclasses import dataclass

from ..game_command_handler import GameCommandHandler
import game.networking.events as E

@dataclass
class JoinRoom:
  join_code: str

class JoinRoomHandler(GameCommandHandler):
  def __init__(self, game):
    super().__init__(JoinRoom, game)

  def handle(self, client_id, command):
    if client_id in self.game.client_room_mapping:
      print(f"[Server] Client {client_id} tried to join room {command.join_code} but was already in a room!")
      return
    if command.join_code not in self.game.rooms:
      print(f"[Server] Client tried to join nonexistent room {command.join_code}!")
      return
    
    print("[Server] Client requested to join room", command.join_code)
    self.game.client_room_mapping[client_id] = command.join_code
    room = self.game.rooms[command.join_code]
    #TODO: check if room is in lobby state - fail if not
    lobby_channel_id = room.state.channel.id
    event = E.RoomJoined(room.channel.id, lobby_channel_id, command.join_code)
    self.game.server.default_channel.send(client_id, event)
    room.channel.clients.add(client_id)
    room.on_join(client_id)