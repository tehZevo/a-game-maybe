from dataclasses import dataclass

from game.components.networking import Id
from game.components.physics import Position
from game.utils import Vector
from ..event_handler import EventHandler
from game.utils import find_entity_by_id

@dataclass
class PositionUpdated:
  id: str
  pos: Vector

class PositionUpdatedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(PositionUpdated)
    self.client_manager = client_manager

  def handle(self, client, event):
    ent = find_entity_by_id(self.client_manager.entity.world, event.id)
    if ent is not None:
      #TODO: lerp?
      ent.get_component(Position).pos = event.pos
