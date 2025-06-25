from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
import game.components as C
from game.utils import Vector
import game.networking.events as E

@dataclass
class HelloWorld:
  pass

class HelloWorldHandler(PlayStateCommandHandler):
  def __init__(self, game_state, save_data):
    super().__init__(HelloWorld, game_state)
    self.save_data = save_data

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    print("[Server], hello world received from", client_id)
    
    world = server_manager.entity.world
    map_id = world.find_component(C.GameMaster).mapdef.id
    server_manager.server.send(client_id, E.TilesetUpdated(map_id))

    world = server_manager.entity.world

    #TODO: call some spawn_player func
    #set up player
    player = world.create_entity([
      C.Networking(),
      C.Position(Vector(2, 2)), #TODO: hardcoded position
      C.Player(),
    ])

    entity_id = player.get_component(C.Networking).id
    server_manager.player_register(client_id, entity_id)
    if client_id in self.save_data.player_data:
      self.save_data.load_player_data(client_id, player)
    else:
      self.save_data.save_player_data(client_id, player)

    #spawn all existing for player
    for networking in world.find_components(C.Networking):
      networking.spawn(client_id)
      networking.on_client_join(client_id)

    #tell the player he controls the newly spawned actor
    server_manager.server.send(client_id, E.PlayerAssigned(entity_id))
