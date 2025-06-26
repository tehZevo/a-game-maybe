from ..armor import Armor
from game.items.slots import ArmorSlot

class Shoes(Armor):
  def __init__(self, **kwargs):
    super().__init__(armor_slot=ArmorSlot.SHOES, **kwargs)
