from items import Skill
from items.slots import SkillSlot

class Alpha(Skill):
  def __init__(self):
    super().__init__()
    self.icon = "assets/items/skills/alpha.png"
    self.slot = SkillSlot.ALPHA
