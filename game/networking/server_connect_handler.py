import game.components as C
from game.utils import Vector

class ServerConnectHandler:
  def __init__(self, save_data):
    self.save_data = save_data
  
  #TODO: we need to manipulate save data here rather than (or in addition to?) directly creating a player
  def handle_connect(self, server_manager, server, client_id):
    from game.networking.events import TilesetUpdated, PlayerAssigned
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = server_manager.entity.world.find_component(C.TilesetPhysics).tileset
    server.send(client_id, TilesetUpdated(ts))

    world = server_manager.entity.world
    #spawn all other existing for player
    for networking in world.find_components(C.Networking):
      networking.spawn(client_id)
      networking.on_client_join(client_id)

    #set up player
    player = world.create_entity([
      C.Networking(),
      C.Position(Vector(2, 2)), #TODO: hardcoded position
      C.Player(),
    ])

    entity_id = player.get_component(C.Networking).id
    server_manager.player_register(client_id, entity_id)
    #TODO: is this necessary?
    self.save_data.save_player_data(client_id, player)

    #tell the player he controls the newly spawned actor
    server.send(client_id, PlayerAssigned(entity_id))