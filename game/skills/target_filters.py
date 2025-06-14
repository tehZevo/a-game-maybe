import game.components as C
from game.components.teams import Team, TeamManager
from game.utils.teams import Disposition
from game.skills.target_type import TargetType

#target filters are of the form (skill) => (actor) => bool

def component_filter(component_type):
  return lambda skill: lambda actor: actor.get_component(component_type) is not None

def distance_filter(radius):
  return lambda skill: lambda actor: skill.get_component(C.Position).pos.distance(actor.get_component(C.Position).pos) <= radius

def target_type_filter(target_type):
  def build_filter(skill):
    user_team = skill.user.get_component(Team).team
    #get team manager here so we arent O(N^2) on potential targets
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
