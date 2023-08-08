import math
from random import gauss

EPSILON = 1e-4

class Vector:
  def random():
    return Vector(gauss(0, 1), gauss(0, 1)).normalized()

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

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
