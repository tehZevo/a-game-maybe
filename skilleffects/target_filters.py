from components import Position

#target filters are of the form (skill, actor) => bool

def component_filter(component_type):
  return lambda skill, actor: actor.get_component(component_type) is not None

def distance_filter(radius):
  def filter(skill, actor):
    skill_pos = skill.get_component(Position).pos
    actor_pos = actor.get_component(Position).pos
    return skill_pos.distance(actor_pos) <= radius
  return filter
  # return lambda skill, actor: skill.get_component(Position).pos.distance(actor.get_component(Position).pos) <= radius
