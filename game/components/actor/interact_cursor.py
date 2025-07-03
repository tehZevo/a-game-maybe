from game.ecs import Component
import game.components as C
import game.data.sprites as S

class InteractCursor(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Position, C.Sprite)

  def start(self):
    self.entity[C.Sprite].set_sprite(S.cursor_16)