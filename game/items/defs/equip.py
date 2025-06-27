from game.stats import Stats
from .itemdef import ItemDef
from game.items.equip_grade import EquipGrade

class Equip(ItemDef):
  def __init__(self, grade=None, stats=None, **kwargs):
    super().__init__(**kwargs)
    self.grade = grade or EquipGrade.UNKNOWN
    self.stats = stats or Stats()
