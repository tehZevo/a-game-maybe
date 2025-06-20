from game.items.rarity import Rarity, rarity_drop_rate
from game.constants import BASE_DROP_RATE

class ItemDef:
  def __init__(self, id=None, rarity=None, icon=None, mini_icon=None, mod_drop_rate=None):
    super().__init__()
    self.id = id
    self.icon = icon or "assets/unknown.png"
    self.mini_icon = mini_icon
    self.rarity = Rarity.COMMON if rarity is None else rarity
    self.mod_drop_rate = 1 if mod_drop_rate is None else mod_drop_rate

  def calc_drop_rate(self):
    return BASE_DROP_RATE * rarity_drop_rate(self.rarity) * self.mod_drop_rate