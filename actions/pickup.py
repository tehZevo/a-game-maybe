from components import Position, DroppedItem, Equips, ItemDropper
from actions import Action
from utils.constants import DT
from utils.find_in_range import find_in_range

PICKUP_RADIUS = 1

#TODO: rename "interact"
class Pickup(Action):
  def __init__(self):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.use_time = 0.5

  def start(self):
    entity_pos = self.entity.get_component(Position).pos

    #find staircases
    #TODO
    # staircases = self.entity.world.find(Stairs)

    #find dropped items nearby
    nearby_items = find_in_range(self.entity.world, DroppedItem, entity_pos, PICKUP_RADIUS)
    if len(nearby_items) > 0:
      item = nearby_items[0]
      item.remove()
      old_equip = self.entity.get_component(Equips).equip(item.get_component(DroppedItem).item)
      #if we had something equipped in that slot, drop it
      if old_equip is not None:
        self.entity.get_component(ItemDropper).drop(old_equip, entity_pos)

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
