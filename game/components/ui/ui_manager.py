from game.ecs import Component
from ..actor.player import Player
from . import HealthBar, ManaBar, Drawable

class UIManager(Component):
  def __init__(self):
    super().__init__()
    self.game_world = None

  def set_player(self, player):
    self.health_bar.get_component(HealthBar).set_player(player)
    self.mana_bar.get_component(ManaBar).set_player(player)

  def start(self):
    #create test health bar
    self.health_bar = self.entity.world.create_entity([HealthBar()])
    self.mana_bar = self.entity.world.create_entity([ManaBar()])

  #TODO: this should probably be moved to renderer, which finds all drawables and draws them...
  def draw(self, screen):
    for drawable in self.entity.world.find_components(Drawable):
      drawable.draw(screen)
