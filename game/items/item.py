#TODO: where to store drop rate?

DEFAULT_DROP_RATE = 1/10

class Item:
  def __init__(self):
    super().__init__()
    self.icon = "assets/unknown.png"
    self.slot = None
    self.drop_rate = DEFAULT_DROP_RATE
