from game.ecs import Component
from game.utils import Vector
import game.components as C

class HealthBar(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Bar)
    self.player = None

  def start(self):
    self.bar = self.get_component(C.Bar)
    self.bar.color = (255, 0, 0)
    self.bar.bg_color = (128, 128, 128)
    self.get_component(C.Position).pos = Vector(0, 0)

  def set_player(self, player):
    self.player = player
    self.player_stats = self.player.get_component(C.Stats)

  def update(self):
    if self.player is None:
      return

    self.bar.max_value = self.player_stats.stats.secondary.hp
    self.bar.value = self.player_stats.hp
