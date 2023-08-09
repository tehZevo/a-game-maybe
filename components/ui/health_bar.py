from .ui_component import UIComponent
from .bar import Bar
from components.actor.stats import Stats

class HealthBar(UIComponent):
  def __init__(self):
    super().__init__()
    self.require(Bar)
    self.player = None

  def start(self):
    self.bar = self.get_component(Bar)

  def set_player(self, player):
    self.player = player
    self.player_stats = self.player.get_component(Stats)

  def update(self):
    if self.player is None:
      return

    self.bar.max_value = self.player_stats.secondary_stats.hp
    self.bar.value = self.player_stats.hp
