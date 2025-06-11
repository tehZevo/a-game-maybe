from dataclasses import dataclass

from ..event_handler import EventHandler
from game import items

#TODO: currently unused, as item sprite and positions are networked
@dataclass
class ItemSpawned:
  id: str
  #class name to create from game.items package
  #because of this, items/__init__.py behaves as a sort of game data registry for items
  item: str

class ItemSpawnedHandler(EventHandler):
  def __init__(self):
    super().__init__(ItemSpawned)

  def handle(self, client_manager, client, event):
    import game.components as C

    #TODO: does this even work? does Id component exist anymore?
    entity = client_manager.entity.world.create_entity([
      C.Id(event.id),
      C.DroppedItem(items.__dict__[event.item]()),
    ])
    print("[Client] item spawned:", event.item)
