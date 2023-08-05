from components import Item

#TODO: make abstract
class Equip(Item):
  def __init__(self):
    super().__init__()
    self.slot = None
