from dataclasses import dataclass

from ..event_handler import EventHandler
from game.components.core import PlayerController

#server tells the player which actor he controls

@dataclass
class PlayerControl:
  id: str

class PlayerControlHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(PlayerControl)
    self.client_manager = client_manager

  def handle(self, client, event):
    print("hey cool")
    entity = self.client_manager.entity.world.create_entity([
      PlayerController(event.id)
    ])
    print("[Client] Controlling actor with id", event.id)
