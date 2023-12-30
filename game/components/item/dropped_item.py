from game.ecs import Component
from ..core import Interactable
import game.components as C

class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(C.Sprite, C.PositionSyncing, C.SpriteSyncing, C.Networking)
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
