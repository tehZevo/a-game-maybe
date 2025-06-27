import game.components as C
from game.components.teams import Team, TeamManager
from game.utils.teams import Disposition
from game.skills.target_type import TargetType
from game.utils import angle_distance

#target filters are of the form (skill) => (actor) => bool

def component_filter(component_type):
  return lambda skill: lambda actor: actor.get_component(component_type) is not None

def distance_filter(radius):
  return lambda skill: lambda actor: skill.entity[C.Position].pos.distance(actor[C.Position].pos) <= radius

def ignore_entities_filter(entities):
  return lambda skill: lambda actor: actor not in entities

def angle_filter(max_angle):
  def calc(source, target):
    ang_to_target = (target[C.Position].pos - source[C.Position].pos).angle()
    source_actor = source[C.Actor]
    dist = angle_distance(source_actor.look_dir.angle(), ang_to_target)
    return dist >= -max_angle and dist <= max_angle
  return lambda skill: lambda actor: calc(skill.user, actor)

def target_type_filter(target_type):
  def build_filter(skill):
    user_team = skill.user.get_component(Team).team
    team_manager = skill.entity.world.find_component(TeamManager)
    def filter(actor):
      target_team = actor.get_component(Team).team
      disposition = team_manager.get_disposition(user_team, target_team)
      if disposition == Disposition.ALLY and target_type == TargetType.ALLY:
        return True
      if disposition == Disposition.ENEMY and target_type == TargetType.ENEMY:
        return True
      return False
    return filter
  return build_filter
