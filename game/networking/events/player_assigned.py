from dataclasses import dataclass

from ..event_handler import EventHandler
from game.components.core import PlayerController

#server tells the client which actor he controls
@dataclass
class PlayerAssigned:
  id: str

class PlayerAssignedHandler(EventHandler):
  def __init__(self):
    super().__init__(PlayerAssigned)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    entity = world.create_entity([C.PlayerController(event.id)])
    #find player, set camera target, and set hud player
    player = client_manager.networked_entities[event.id]
    world.find_component(C.Camera).target = player
    #TODO: this feels weird
    world.find_component(C.GameMaster).game.hud.get_component(C.HUD).set_player(player)

    print("[Client] Controlling actor with id", event.id)
