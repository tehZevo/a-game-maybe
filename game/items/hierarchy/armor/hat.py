from ..armor import Armor
from game.items.slots import ArmorSlot

class Hat(Armor):
  def __init__(self, **kwargs):
    super().__init__(armor_slot=ArmorSlot.HAT, **kwargs)
