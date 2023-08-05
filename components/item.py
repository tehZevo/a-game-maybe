from ecs import Component

#TODO: where to store drop rate?

class Item(Component):
  def __init__(self):
    super().__init__()
    self.icon = "assets/item.png"
