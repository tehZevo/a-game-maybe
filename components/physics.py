from ecs import Component
from components import Position
from utils import Vector
from utils.constants import DT

DEFAULT_MASS = 1
DEFAULT_FRICTION = 0.5

#TODO: could really use a basic vector class
class Physics(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.mass = DEFAULT_MASS
    self.friction = DEFAULT_FRICTION
    self.force = Vector()
    self.vel = Vector()

  def apply_force(self, fx, fy):
    self.force = self.force + Vector(fx, fy)

  def update(self):
    pos = self.get_component(Position)
    #TODO: return vector from get_pos?
    x, y = pos.get_pos()
    p = Vector(x, y)

    #integrate
    self.vel = self.vel + self.force / self.mass * DT
    p = p + self.vel * DT
    pos.set_pos(p.x, p.y)

    #reset force
    self.force = Vector()

    #apply friction
    self.vel = self.vel / (1 + self.friction)
