from game.components.skill import Skill
from game.components.actor import Actor
import game.components as C
from .skill_effect import SkillEffect

#TODO: max targets
class Target(SkillEffect):
  def __init__(self, filters=[], children=[]):
    super().__init__()
    self.filters = filters
    self.children = children

  def start(self, skill):
    #find all actors in range
    actors = skill.entity.world.find(Actor)
    #filter actors based on filter condition(s)
    skill_comp = skill.entity.get_component(Skill)
    for filter in self.filters:
      actors = [a for a in actors if filter(skill_comp)(a)]

    for target in actors:
      for child in self.children:
        #create new skill effect with target
        skill.entity.world.create_entity([
          C.Position(target.get_component(C.Position).pos),
          Skill(child, skill.user, skill.entity, target=target) #TODO: set parent?
        ])
