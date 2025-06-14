from ..equip import Equip

class Armor(Equip):
  def __init__(self, armor_slot=None, **kwargs):
    super().__init__(**kwargs)
    self.armor_slot = armor_slot
