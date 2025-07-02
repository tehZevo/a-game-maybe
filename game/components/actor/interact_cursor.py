from game.ecs import Component
import game.components as C
from game.utils import Vector
from game.utils.find_in_range import find_in_range
from game.constants import DT, INTERACT_RADIUS, INTERACT_CURSOR_UPDATE_TIME, INTERACT_CURSOR_DISTANCE

class InteractCursor(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Actor, C.Position)
    self.interact_target = None
    self.time_since_last_update = 0

  def update(self):
    self.time_since_last_update += DT
    if self.time_since_last_update < INTERACT_CURSOR_UPDATE_TIME:
      return
    
    self.time_since_last_update = 0
    my_pos = self.entity[C.Position].pos
    look_dir = self.entity[C.Actor].look_dir
    interact_center_pos = my_pos + look_dir * INTERACT_CURSOR_DISTANCE

    interactables = find_in_range(self.entity.world, C.Interactable, interact_center_pos, INTERACT_RADIUS, sort=True)
    if len(interactables) == 0:
      return
    
    self.interact_target = interactables[0]
    #TODO: send update to server if changed