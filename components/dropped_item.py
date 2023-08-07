from ecs import Component
from components.interactable import Interactable

class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(Sprite)
    self.item = item

  def start(self):
    self.get_component(Sprite).set_sprite(self.item.icon)

  def interact(self, entity):
    #TODO: reee
    from components.item_dropper import ItemDropper
    old_equip = entity.get_component(Equips).equip(self.item)
    #if we had something equipped in that slot, drop it
    if old_equip is not None:
      entity.get_component(ItemDropper).drop(old_equip, entity.get_component(Position).pos)

    self.entity.remove()

#TODO: reee
from components.sprite import Sprite
from components.position import Position
from components.equips import Equips
