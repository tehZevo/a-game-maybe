from .slots import ArmorSlot
from . import Armor

class Hat(Armor):
  def __init__(self):
    super().__init__()
    self.icon = "assets/items/armor/hat.png"
    self.slot = ArmorSlot.HAT
