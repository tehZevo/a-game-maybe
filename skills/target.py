import copy

from ecs import Entity
from components import Skill, Actor
from skills import SkillEffect

#TODO: maybe have target filters passed to a target?
#TODO: actually, they probably need to be classes so they can be created from game data
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
        #TODO: need to actually create a copy?
        child = copy.copy(child) #TODO: test
        child.target = target
        self.entity.world.create_entity([Skill(child)])
