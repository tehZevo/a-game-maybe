from ..armor import Armor
from game.items.slots import ArmorSlot

class Gloves(Armor):
  def __init__(self, **kwargs):
    super().__init__(armor_slot=ArmorSlot.GLOVES, **kwargs)
