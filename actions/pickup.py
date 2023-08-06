from components import Position, DroppedItem, Equip, Equipment, ItemDropper
from actions import Action
from utils.constants import DT

PICKUP_RADIUS = 1

class Pickup(Action):
  def __init__(self):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.use_time = 0.5

  def start(self):
    entity_pos = self.entity.get_component(Position).pos

    #find dropped items nearby
    items = self.entity.world.find(DroppedItem)
    for item in items:
      #skip non-equip items TODO: ?? what about skills? technically arent all items equips?
      if item.get_component(Equip) is None:
        continue

      item_pos = item.get_component(Position).pos
      #if within radius, pickup
      if item_pos.distance(entity_pos) <= PICKUP_RADIUS:
        equip_comp = item.get_component(Equip)
        item.remove()
        old_equip = self.entity.get_component(Equipment).set_equip(equip_comp.slot, item)
        #if we had something equipped in that slot, drop it
        if old_equip is not None:
          self.entity.get_component(ItemDropper).drop(old_equip.get_component(Equip), entity_pos)
        break

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
