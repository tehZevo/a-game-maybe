from ecs import Component
from .position import Position
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

  def apply_force(self, force):
    self.force = self.force + force

  def update(self):
    pc = self.get_component(Position)

    #integrate
    self.vel = self.vel + self.force / self.mass * DT
    pc.pos = pc.pos + self.vel * DT

    #reset force
    self.force = Vector()

    #apply friction
    self.vel = self.vel / (1 + self.friction)
