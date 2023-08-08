from components.physics.position import Position

#target filters are of the form (skill, actor) => bool

def component_filter(component_type):
  return lambda skill, actor: actor.get_component(component_type) is not None

def distance_filter(radius):
  return lambda skill, actor: skill.get_component(Position).pos.distance(actor.get_component(Position).pos) <= radius
