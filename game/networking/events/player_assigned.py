from dataclasses import dataclass

from ..event_handler import EventHandler
from game.components.core import PlayerController
from game.components.graphics import Camera
from game.utils import find_entity_by_id
#server tells the player which actor he controls

@dataclass
class PlayerAssigned:
  id: str

class PlayerAssignedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(PlayerAssigned)
    self.client_manager = client_manager

  def handle(self, client, event):
    world = self.client_manager.entity.world
    entity = world.create_entity([PlayerController(event.id)])
    #find player and set camera target
    player = find_entity_by_id(world, event.id)
    self.client_manager.entity.world.find_component(Camera).target = player
    print("[Client] Controlling actor with id", event.id)
