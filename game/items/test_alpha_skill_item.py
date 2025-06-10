from . import SkillItem
from game.skills import test_alpha_skill

class TestAlphaSkillItem(SkillItem):
  def __init__(self):
    super().__init__(test_alpha_skill)
