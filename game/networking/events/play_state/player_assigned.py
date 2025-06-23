from dataclasses import dataclass

from game.networking import PlayStateEventHandler
from game.components.core import PlayerController

#server tells the client which actor he controls
@dataclass
class PlayerAssigned:
  id: str

class PlayerAssignedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(PlayerAssigned, game_state)

  def handle(self, event):
    import game.components as C
    client_manager = self.game_state.client_manager
    world = client_manager.entity.world
    entity = world.create_entity([C.PlayerController(event.id)])
    #find player, set camera target, and set hud player
    player = client_manager.networked_entities[event.id]
    world.find_component(C.Camera).target = player
    #TODO: this feels weird
    world.find_component(C.GameMaster).game.hud.get_component(C.HUD).set_player(player)

    print("[Client] Controlling actor with id", event.id)
