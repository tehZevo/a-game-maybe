from dataclasses import dataclass

from ..event_handler import EventHandler
from ..component_registry import get_component_classes

#TODO: make this a generic entity_spawned?
#TODO: then how would i choose which components to create on the client side?

@dataclass
class EntitySpawned:
  id: str
  component_data: dict

class EntitySpawnedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(EntitySpawned)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: circular import
    from game.components.networking import Id
    classes = get_component_classes()
    #construct components
    classes = get_component_classes()
    components = [classes[k](**v) for k, v in event.component_data.items()]
    #create an entity with the provided id and components
    entity = self.client_manager.entity.world.create_entity([
      Id(event.id),
      *components
    ])
    print(f"[Client] Entity spawned with id {event.id}:", entity)
