from dataclasses import dataclass

from ..event_handler import EventHandler
from ..component_registry import get_component_classes
import game.components as C

#TODO: need the ability to spawn entities on client without networking eg particle emitters or other effects (vfx)

@dataclass
class EntitySpawned:
  id: str
  component_names: list

class EntitySpawnedHandler(EventHandler):
  def __init__(self):
    super().__init__(EntitySpawned)

  def handle(self, client_manager, client, event):
    #construct components
    classes = get_component_classes()
    components = [classes[k]() for k in event.component_names]
    #create an entity with the provided id and components
    entity = client_manager.entity.world.create_entity([
      C.Networking(event.id),
      *components
    ])
    # print(f"[Client] Entity spawned with id {event.id}:", entity)