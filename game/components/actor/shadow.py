from game.ecs import Component
import game.components as C
from game.components.graphics import Drawable
from game.utils.image_cache import get_image
from game.utils import Vector

class Shadow(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.require(C.Position)

  def draw(self, renderer):
    image = get_image("assets/shadow.png")
    #TODO: hardcoded offset
    renderer.draw(image, self.entity[C.Position].pos + Vector(0, -3/16), alpha=0.5, offset=Vector(0, 5/16))