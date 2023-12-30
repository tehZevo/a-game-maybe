from game.ecs import Component
from ..core import Interactable
from ..networking import Networkable
import game.components as C

#currently not networkable, but its entity is networked (sprite, position synced)
class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(C.Sprite, C.Networked)
    self.item = item

  def start(self):
    self.get_component(C.Sprite).set_sprite(self.item.icon)

  def interact(self, entity):
    #TODO: have equips component drop the item instead?
    old_equip = entity.get_component(C.Equips).equip(self.item)
    #if we had something equipped in that slot, drop it
    if old_equip is not None:
      entity.get_component(C.ItemDropper).drop(old_equip, entity.get_component(C.Position).pos)

    self.entity.remove()
