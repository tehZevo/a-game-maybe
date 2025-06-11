from dataclasses import dataclass

from ..command_handler import CommandHandler
import game.components as C
from game.utils import Vector

@dataclass
class Sync:
  pass

class SyncHandler(CommandHandler):
  def __init__(self, save_data):
    super().__init__(Sync)
    self.save_data = save_data

  def handle(self, server_manager, server, client_id, command):
    print("[Server], sync received from", client_id)
    from game.networking.events import TilesetUpdated, PlayerAssigned
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = server_manager.entity.world.find_component(C.TilesetPhysics).tileset
    server.send(client_id, TilesetUpdated(ts))

    world = server_manager.entity.world

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
    server.send(client_id, PlayerAssigned(entity_id))
