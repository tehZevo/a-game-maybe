import uuid

from game.ecs import Component

class Id(Component):
  def __init__(self, id=None):
    super().__init__()
    self.id = str(uuid.uuid4()) if id is None else id
