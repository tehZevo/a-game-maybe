import math

EPSILON = 1e-4

class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def normalized(self):
    x, y = self.x, self.y
    mag = math.sqrt(x ** 2 + y ** 2)
    if mag < EPSILON:
      return Vector(0, 0)

    x = self.x / mag
    y = self.y / mag

    return Vector(x, y)

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

  def copy(self):
    return Vector(self.x, self.y)

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
