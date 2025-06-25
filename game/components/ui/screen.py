from game.ecs import Component
import game.components as C
from game.components.graphics import Drawable
from game.components.core import KeyHandler

class Screen(Component, KeyHandler, Drawable):
  def __init__(self):
    super().__init__()
  
  def handle_keys(self, kb):
    pass
  
  def draw(self, renderer):
    pass