from game.ecs import Component
from ..core import Interactable
from ..graphics.sprite import Sprite
from ..physics.position import Position
from ..networking import DroppedItemNetworking
from . import Equips

class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(Sprite)
    self.require(DroppedItemNetworking)
    self.item = item

  def start(self):
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
