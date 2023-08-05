from ecs import Component
from components import Position

DEFAULT_MASS = 1
DEFAULT_FRICTION = 0.5

#TODO: could really use a basic vector class
class Physics(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.mass = DEFAULT_MASS
    self.friction = DEFAULT_FRICTION
    self.force = [0, 0]
    self.vel = [0, 0]

  def apply_force(self, fx, fy):
    self.force[0] += fx
    self.force[1] += fy

  def update(self):
    pos = self.get_component(Position)
    x, y = pos.get_pos()

    #integrate
    self.vel[0] += self.force[0] / self.mass
    self.vel[1] += self.force[1] / self.mass
    x += self.vel[0]
    y += self.vel[1]
    pos.set_pos(x, y)

    #reset force
    self.force = [0, 0]

    #apply friction
    self.vel[0] /= 1 + self.friction
    self.vel[1] /= 1 + self.friction
