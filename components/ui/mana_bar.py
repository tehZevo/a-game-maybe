from ecs import Component
from .bar import Bar
from components.actor.stats import Stats
from components.physics.position import Position
from utils import Vector

class ManaBar(Component):
  def __init__(self):
    super().__init__()
    self.require(Bar)
    self.player = None

  def start(self):
    self.bar = self.get_component(Bar)
    self.bar.color = (0, 0, 255)
    self.bar.bg_color = (128, 128, 128)
    self.get_component(Position).pos = Vector(0, 16)

  def set_player(self, player):
    self.player = player
    self.player_stats = self.player.get_component(Stats)

  def update(self):
    if self.player is None:
      return

    self.bar.max_value = self.player_stats.secondary_stats.mp
    self.bar.value = self.player_stats.mp
