from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler

@dataclass
class PositionUpdated:
  id: str
  pos: Vector

class PositionUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(PositionUpdated)

  def handle(self, client_manager, client, event):
    from game.components.physics import Position
    #TODO: this is caused by entities not being on client yet.. need to sync them when client first "sees" them
    # this either means sending actor spawned for all ents upon player join, OR having other actors/networked components spawn/despawn themselves on the client
    if event.id not in client_manager.networked_entities:
      #print("trying to update entity position with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.networked_entities[event.id]
    if ent is not None:
      #TODO: lerp?
      ent.get_component(Position).pos = event.pos
