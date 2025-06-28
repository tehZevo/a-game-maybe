from game.ecs import Component
from ..teams.team_manager import TeamManager, Disposition

class GameMaster(Component):
  def __init__(self, game, mapdef):
    super().__init__()
    self.require(TeamManager)
    self.game = game
    self.mapdef = mapdef

  def start(self):
    #pit enemies against players
    teams = self.get_component(TeamManager)
    teams.set_disposition("player", "enemy", Disposition.ENEMY)
    teams.set_disposition("player", "player", Disposition.ALLY)
