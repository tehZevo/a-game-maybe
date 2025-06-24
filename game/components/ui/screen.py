from game.ecs import Component
import game.components as C

from game.components.core import KeyHandler

class Screen(Component, KeyHandler):
  def __init__(self):
    super().__init__()