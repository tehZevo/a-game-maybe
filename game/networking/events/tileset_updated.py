from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset
from game.components.graphics import BakedTileset
from game.components.tiles import TilesetPhysics

@dataclass
class TilesetUpdated:
  tileset: Tileset

class TilesetUpdatedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(TilesetUpdated)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: should i delete the old ones first?
    world = self.client_manager.entity.world
    world.create_entity([
      BakedTileset(event.tileset),
    ])
    world.create_entity([
      TilesetPhysics(event.tileset),
    ])
