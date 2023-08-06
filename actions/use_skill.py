from components import Skill, Position
from actions import Action
from utils.constants import DT

class UseSkill(Action):
  def __init__(self, effect):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.effect = effect
    #TODO: hardcoded use time
    self.use_time = 0.5

  def start(self):
    #create skill effect in world at user position
    self.entity.world.create_entity([
      Position(self.entity.get_component(Position).pos),
      Skill(self.effect)
    ])

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
