from . import Item

class SkillItem(Item):
  def __init__(self, skilldef):
    super().__init__()
    self.skilldef = skilldef
    self.icon = self.skilldef.icon #:|
