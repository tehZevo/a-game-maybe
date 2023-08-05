from components.items import Equip
from components.equipment import EquipmentSlot

class Armor(Equip):
  def __init__(self):
    super().__init__()
    self.icon = "assets/armor.png"
    self.slot = EquipmentSlot.ARMOR
