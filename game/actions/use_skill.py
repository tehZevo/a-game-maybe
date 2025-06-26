from game.components.skill.skill import Skill
import game.components as C
from game.components.actor.stats import Stats
from game.constants import DT
from . import Action
from game.data.registry import get_skill

class UseSkill(Action):
  def deserialize(action_data):
    skilldef = get_skill(action_data["skilldef"])
    return UseSkill(skilldef)

  def __init__(self, skilldef):
    super().__init__()
    self.interruptible = False
    self.active = False
    self.skilldef = skilldef
    self.use_time = self.skilldef.use_time
  
  def serialize(self):
    return {"skilldef": self.skilldef.id}

  def start(self):
    stats = self.entity.get_component(Stats)

    #check hp/mp cost
    if stats.hp < self.skilldef.hp_cost:
      return
    if stats.mp < self.skilldef.mp_cost:
      return

    self.active = True

    #deduct hp/mp cost
    stats.add_hp(-self.skilldef.hp_cost)
    stats.add_mp(-self.skilldef.mp_cost)

    for effect in self.skilldef.effects:
      #create skill effect in world at user position
      self.entity.world.create_entity([
        C.Position(self.entity.get_component(C.Position).pos),
        Skill(effect, user=self.entity)
      ])

  def update(self):
    if not self.active:
      return

    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
