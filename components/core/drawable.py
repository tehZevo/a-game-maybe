from ecs import Component

#TODO: move to render even thought its an iface?
class Drawable:
  def __init__(self):
    pass

  def draw(self, screen, offset=None):
    raise NotImplementedError
