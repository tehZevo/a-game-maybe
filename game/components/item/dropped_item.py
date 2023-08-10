from ecs import Component
from components.core import Interactable
from components.graphics.sprite import Sprite
from components.physics.position import Position
from components.item.equips import Equips

class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(Sprite)
    self.item = item

  def start(self):
    self.get_component(Sprite).set_sprite(self.item.icon)

  def interact(self, entity):
    #TODO: reee
    from components.item.item_dropper import ItemDropper
    old_equip = entity.get_component(Equips).equip(self.item)
    #if we had something equipped in that slot, drop it
    if old_equip is not None:
      entity.get_component(ItemDropper).drop(old_equip, entity.get_component(Position).pos)

    self.entity.remove()
