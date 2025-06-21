from game.ecs import Component
import game.components as C
from game.constants import MAX_DROPPED_ITEMS

class DroppedItemManager(Component):
  def __init__(self):
    super().__init__()

  def update(self):
    items = self.entity.world.find(C.DroppedItem)
    items_to_destroy = items[:-MAX_DROPPED_ITEMS]
    for item in items_to_destroy:
      print("[Server] Removing old dropped item:", item[C.DroppedItem].item.id)
      item.remove()
