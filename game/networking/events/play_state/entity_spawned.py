from dataclasses import dataclass

from game.networking import PlayStateEventHandler
from game.networking.component_registry import get_component_classes
import game.components as C

#TODO: need the ability to spawn entities on client without networking eg particle emitters or other effects (vfx)

@dataclass
class EntitySpawned:
  id: str
  component_names: list

class EntitySpawnedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(EntitySpawned, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    #construct components
    classes = get_component_classes()
    components = [classes[k]() for k in event.component_names]
    #create an entity with the provided id and components
    entity = client_manager.entity.world.create_entity([
      C.Networking(event.id),
      *components
    ])
