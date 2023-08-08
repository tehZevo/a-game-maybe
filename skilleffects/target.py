import copy

from ecs import Entity
from components import Skill, Actor, Position
from skilleffects import SkillEffect

#TODO: max targets
class Target(SkillEffect):
  def __init__(self, filters=[], children=[]):
    super().__init__()
    self.filters = filters
    self.children = children

  def start(self):
    #find all actors in range
    actors = self.entity.world.find(Actor)
    #filter actors based on filter condition(s)
    for filter in self.filters:
      actors = [a for a in actors if filter(self.entity, a)]

    for target in actors:
      for child in self.children:
        #create new skill effect with target
        child = copy.copy(child)
        child.target = target
        self.entity.world.create_entity([
          Position(target.get_component(Position).pos),
          Skill(child, self.user, self.entity)
        ])
