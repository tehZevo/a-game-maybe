from . import Action
from game.utils.constants import DT
from game.utils.find_in_range import find_in_range
import game.components as C
from game.components.core.interactable import Interactable

INTERACT_RADIUS = 1

class Interact(Action):
  def __init__(self):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.use_time = 0.5

  def start(self):
    entity_pos = self.entity.get_component(C.Position).pos

    #TODO: sort by distance
    interactables = find_in_range(self.entity.world, Interactable, entity_pos, INTERACT_RADIUS)
    if len(interactables) > 0:
      interactable = interactables[0]
      for component in interactable.components.values():
        if issubclass(component.__class__, Interactable):
          component.interact(self.entity)

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
