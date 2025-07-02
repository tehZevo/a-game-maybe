import game.components as C
from ..skill_effect import SkillEffect

def apply_target(skill, filters, max_targets, children):
  #filter actors based on filter condition(s)
  actors = skill.entity.world.find(C.Actor)
  for filter in filters:
    actors = [a for a in actors if filter(skill)(a)]

  actors = actors if max_targets is None else actors[:max_targets]
  
  for target in actors:
    for child in children:
      #create new skill effect with target
      skill.entity.world.create_entity([
        C.Position(target[C.Position].pos),
        C.Skill(child, skill.user, skill.entity, target=target)
      ])
  
  return actors

#TODO: max targets
class Target(SkillEffect):
  def __init__(self, filters=[], max_targets=1, children=[]):
    super().__init__()
    if not isinstance(children, (list, tuple)):
      children = [children]
    if not isinstance(filters, (list, tuple)):
      filters = [filters]
    self.filters = filters
    self.children = children
    self.max_targets = max_targets

  def start(self, skill):
    apply_target(skill, self.filters, self.max_targets, self.children)
