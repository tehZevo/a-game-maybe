from dataclasses import dataclass
import math
from random import gauss
import random

EPSILON = 1e-4

@dataclass
class Vector:
  x: float
  y: float

  #TODO: meh
  def from_pygame(v):
    return Vector(v.x, v.y)

  def random():
    return Vector(gauss(0, 1), gauss(0, 1)).normalized()
  
  def random_disc(r=1):
    #TODO: not uniform but good enough for now
    dist = random.random()
    return Vector.random() * dist

  def __init__(self, x=0, y=0):
    super().__init__()
    self.x = x
    self.y = y

  #TODO: meh
  def to_pygame(self):
    from pygame import Vector2
    return Vector2(self.x, self.y)

  def angle(self):
    return math.atan2(self.y, self.x) / (2 * math.pi) * 360
  
  def normalized(self):
    mag = self.magnitude()
    if mag < EPSILON:
      return Vector(0, 0)

    return Vector(
      self.x / mag,
      self.y / mag
    )

  def abs(self):
    return Vector(abs(self.x), abs(self.y))

  def clip(self, vmin, vmax):
    return Vector(
      max(vmin.x, min(self.x, vmax.x)),
      max(vmin.y, min(self.y, vmax.y)),
    )

  def magnitude(self):
    return math.sqrt(self.x ** 2 + self.y ** 2)

  def tolist(self):
    return [self.x, self.y]

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

  def copy(self):
    return Vector(self.x, self.y)

  def __neg__(self):
    return Vector(-self.x, -self.y)

  def __add__(self, other):
    if type(other) == Vector:
      return Vector(self.x + other.x, self.y + other.y)
    if isinstance(other, (int, float)):
      return Vector(self.x + other, self.y + other)
    raise ValueError(f"Unsupported type in add: {type(other)}")

  def __sub__(self, other):
    if type(other) == Vector:
      return Vector(self.x - other.x, self.y - other.y)
    if isinstance(other, (int, float)):
      return Vector(self.x - other, self.y - other)
    raise ValueError(f"Unsupported type in sub: {type(other)}")

  def __mul__(self, other):
    if type(other) == Vector:
      return Vector(self.x * other.x, self.y * other.y)
    if isinstance(other, (int, float)):
      return Vector(self.x * other, self.y * other)
    raise ValueError(f"Unsupported type in mul: {type(other)}")

  def __truediv__(self, other):
    if type(other) == Vector:
      return Vector(self.x / other.x, self.y / other.y)
    if isinstance(other, (int, float)):
      return Vector(self.x / other, self.y / other)
    raise ValueError(f"Unsupported type in div: {type(other)}")

  def __str__(self):
    return f"[Vector] {self.x} {self.y}"

Vector.ZERO = Vector(0, 0)
Vector.X = Vector(1, 0)
Vector.Y = Vector(0, 1)
