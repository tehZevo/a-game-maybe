from dataclasses import dataclass

from ..event_handler import EventHandler
from game.components.core import PlayerController

#server tells the client which actor he controls
@dataclass
class PlayerAssigned:
  id: str

class PlayerAssignedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(PlayerAssigned)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: circular imports
    from game.components.graphics import Camera
    from game.components.core import GameMaster
    from game.components.ui import UIManager
    world = self.client_manager.entity.world
    entity = world.create_entity([PlayerController(event.id)])
    #find player, set camera target, and set ui manager player
    player = self.client_manager.networked_entities[event.id]
    world.find_component(Camera).target = player
    #TODO: this feels weird
    world.find_component(GameMaster).game.ui_manager.get_component(UIManager).set_player(player)

    print("[Client] Controlling actor with id", event.id)
