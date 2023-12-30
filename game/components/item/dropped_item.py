from game.ecs import Component
from ..core import Interactable
from ..networking import Networkable
import game.components as C
from . import Equips

class DroppedItem(Component, Interactable, Networkable):
  def __init__(self, item):
    super().__init__()
    #TODO: circular import
    from ..graphics.sprite import Sprite
    from ..networking import DroppedItemNetworking
    self.require(Sprite, DroppedItemNetworking)
    self.item = item

  def melt(self):
    return {
      "item": self.item
    }

  def start(self):
    #TODO: circular import
    from ..graphics.sprite import Sprite
    self.get_component(Sprite).set_sprite(self.item.icon)

  def interact(self, entity):
    #TODO: have equips drop the item? might fix circular import
    #TODO: circular import
    from . import ItemDropper
    old_equip = entity.get_component(Equips).equip(self.item)
    #if we had something equipped in that slot, drop it
    if old_equip is not None:
      entity.get_component(ItemDropper).drop(old_equip, entity.get_component(Position).pos)

    self.entity.remove()
