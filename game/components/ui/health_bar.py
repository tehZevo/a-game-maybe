from ecs import Component
from .bar import Bar
from components.actor.stats import Stats
from components.physics.position import Position
from utils import Vector

class HealthBar(Component):
  def __init__(self):
    super().__init__()
    self.require(Bar)
    self.player = None

  def start(self):
    self.bar = self.get_component(Bar)
    self.bar.color = (255, 0, 0)
    self.bar.bg_color = (128, 128, 128)
    self.get_component(Position).pos = Vector(0, 0)

  def set_player(self, player):
    self.player = player
    self.player_stats = self.player.get_component(Stats)

  def update(self):
    if self.player is None:
      return

    self.bar.max_value = self.player_stats.secondary_stats.hp
    self.bar.value = self.player_stats.hp
