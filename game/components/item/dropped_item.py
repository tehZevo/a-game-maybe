from game.ecs import Component
from ..core import Interactable
import game.components as C
from game.utils.constants import ITEM_PUSH_DISTANCE, ITEM_PUSH_FORCE

class DroppedItem(Component, Interactable):
  def __init__(self, item):
    super().__init__()
    self.require(C.Icon, C.Physics, C.Collisions, C.PositionSyncing, \
      C.VelocitySyncing, C.IconSyncing, C.Networking)
    self.item = item

  def start(self):
    self.get_component(C.Icon).set_image(self.item.icon)
  
  def update(self):
    #currently dropped items only exist on the server
    #move this logic to update_server when that changes
    my_pos = self.get_component(C.Position).pos
    my_phys = self.get_component(C.Physics)
    other_items = [c.entity for c in self.entity.world.find_components(DroppedItem) if c != self]
    for e in other_items:
      other_pos = e.get_component(C.Position).pos
      dist = my_pos.distance(other_pos)
      if dist <= ITEM_PUSH_DISTANCE:
        push_dir = (my_pos - other_pos).normalized()
        my_phys.apply_force(push_dir * ITEM_PUSH_FORCE)

  def interact(self, entity):
    #TODO: have equips component drop the item instead?
    old_equip = entity.get_component(C.Equips).equip(self.item)
    #if we had something equipped in that slot, drop it
    if old_equip is not None:
      entity.get_component(C.ItemDropper).drop(old_equip, entity.get_component(C.Position).pos.copy())

    self.entity.remove()
