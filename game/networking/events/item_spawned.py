from dataclasses import dataclass

from ..event_handler import EventHandler
from game import items

@dataclass
class ItemSpawned:
  id: str
  #class name to create from game.items package
  #because of this, items/__init__.py behaves as a sort of game data registry for items
  item: str

class ItemSpawnedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(ItemSpawned)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: circular import
    from game.components.networking import Id
    from game.components.item import DroppedItem

    entity = self.client_manager.entity.world.create_entity([
      Id(event.id),
      DroppedItem(items.__dict__[event.item]()),
    ])
    print("[Client] item spawned:", event.item)
