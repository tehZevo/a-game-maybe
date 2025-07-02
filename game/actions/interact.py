from . import Action
from game.constants import DT
import game.components as C
from game.components.core.interactable import Interactable

class Interact(Action):
  def deserialize(action_data):
    return Interact()
    
  def __init__(self):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.use_time = 0

  def serialize(self):
    return {}

  def start(self):
    cursor = self.entity[C.InteractCursor]
    target = cursor and cursor.interact_target
    if target is None:
      return
    
    for component in target.components.values():
      if issubclass(component.__class__, Interactable):
        component.interact(self.entity)

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
