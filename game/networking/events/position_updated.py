from dataclasses import dataclass

from game.components.networking import Id
from game.components.physics import Position
from game.utils import Vector
from ..event_handler import EventHandler

@dataclass
class PositionUpdated:
  id: str
  pos: Vector

class PositionUpdatedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(PositionUpdated)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: need util for finding entities by specific id
    # also this is really expensive...
    #two solutions:
    #A: make "id" a property of ecs entity (and allow creation of entity with specific id)
    #B: keep track of networked entities in a component
    # (i kinda like B)
    ents = self.client_manager.entity.world.find(Id)
    ents = {ent.get_component(Id).id: ent for ent in ents}
    ent = ents[event.id]
    #TODO: lerp?
    ent.get_component(Position).pos = event.pos
