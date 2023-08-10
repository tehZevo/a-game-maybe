from ecs import Component
from components.teams.team_manager import TeamManager, Disposition

class GameMaster(Component):
  def __init__(self, game):
    super().__init__()
    self.require(TeamManager)
    self.game = game

  def start(self):
    #pit enemies against players
    teams = self.get_component(TeamManager)
    teams.set_disposition("player", "enemy", Disposition.ENEMY)
