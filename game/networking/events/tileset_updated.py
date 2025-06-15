from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset, PackedTileset
from game.data.registry import get_map

#TODO: for now, we'll add mapdef to tileset updated, since it's sent on sync
#TODO: later, move map_id to its own map updated (or worldopened?)
@dataclass
class TilesetUpdated:
  tileset: PackedTileset
  map_id: str

class TilesetUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(TilesetUpdated)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    #set gamemaster's mapdef so tileset can be baked
    game_master = world.find_component(C.GameMaster)
    game_master.mapdef = get_map(event.map_id)

    #unpack and load tileset
    ts = Tileset.unpack(event.tileset)
    world.create_entity([C.BakedTileset(ts)])
    world.create_entity([C.TilesetPhysics(ts)])
