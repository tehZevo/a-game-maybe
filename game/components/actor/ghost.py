from game.ecs import Component
import game.data.sprites as Sprites
import game.components as C

class Ghost(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Position, C.Sprite, C.SpriteSyncing, C.PositionSyncing)

  def start(self):
    sprite = self.get_component(C.Sprite)
    sprite.set_sprite(Sprites.ghost)
  
  def update(self):
    pos = self.get_component(C.Position)