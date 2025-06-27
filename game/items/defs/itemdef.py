from game.items.rarity import Rarity, rarity_drop_rate
from game.constants import BASE_DROP_RATE

class ItemDef:
  def __init__(self, id=None, rarity=None, icon=None, mini_icon=None):
    super().__init__()
    self.id = id
    self.icon = icon or "assets/unknown.png"
    self.mini_icon = mini_icon
    self.rarity = Rarity.COMMON if rarity is None else rarity

  def calc_drop_rate(self):
    return BASE_DROP_RATE * rarity_drop_rate(self.rarity)