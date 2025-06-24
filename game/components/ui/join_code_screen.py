import game.components as C

from game.utils import Vector
from .screen import Screen

class JoinCodeScreen(Screen):
  def __init__(self, game):
    super().__init__()
    #TODO: dunno how i feel about storing game here.. maybe a cb instead?
    self.game = game
  
  def start(self):
    self.join_code_field = self.entity.world.create_entity([
      C.Position(Vector(32, 32)),
      C.TextField(lambda join_code: self.game.join_game(join_code), draw_length=6, max_length=5)
    ])

  def on_destroy(self):
    self.join_code_field.remove()

  def handle_keys(self, kb):
    self.join_code_field[C.TextField].handle_keys(kb)