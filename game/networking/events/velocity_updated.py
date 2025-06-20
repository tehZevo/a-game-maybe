from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler

@dataclass
class VelocityUpdated:
  id: str
  vel: Vector

class VelocityUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(VelocityUpdated)

  def handle(self, client_manager, client, event):
    from game.components.physics import Physics
    if event.id not in client_manager.networked_entities:
      return
    ent = client_manager.networked_entities[event.id]
    ent.get_component(Physics).vel = event.vel
