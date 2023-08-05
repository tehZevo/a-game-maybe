from components.items import Equip
from components.equipment import EquipmentSlot

class Hat(Equip):
  def __init__(self):
    super().__init__()
    self.icon = "assets/hat.png"
    self.slot = EquipmentSlot.HAT
