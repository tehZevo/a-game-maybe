from components import Skill, Position
from actions import Action
from utils.constants import DT

class UseSkill(Action):
  def __init__(self, effects):
    super().__init__()
    self.interruptible = False
    self.active = True
    #TODO: really should wrap effects in a skill object
    self.effects = [effects] if type(effects) != list else effects
    #TODO: hardcoded use time (should be member of skill class)
    self.use_time = 0.5

  def start(self):
    for effect in self.effects:
      #create skill effect in world at user position
      self.entity.world.create_entity([
        Position(self.entity.get_component(Position).pos),
        Skill(effect, user=self.entity)
      ])

  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
