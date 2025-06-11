from game.ecs import Component
from game.utils import Vector
from ..actor import Stats
from ..physics import Position
from . import Bar

#TODO
class HUD(UIComponent):
  def __init__(self):
    super().__init__()
    self.player = None

  def start(self):
    #TODO: create health bars, items, skills
    pass

  def set_player(self, player):
    self.player = player
    self.player_stats = self.player.get_component(Stats)
    #TODO: set player of other stuff we control
