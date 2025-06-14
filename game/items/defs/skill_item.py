from .itemdef import Itemdef

class SkillItem(Itemdef):
  def __init__(self, skilldef, **kwargs):
    kwargs.setdefault("icon", skilldef.icon)
    super().__init__(**kwargs)
    self.skilldef = skilldef