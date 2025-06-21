from .itemdef import ItemDef

class SkillItem(ItemDef):
  def __init__(self, skilldef, **kwargs):
    kwargs.setdefault("icon", skilldef.icon)
    kwargs.setdefault("mini_icon", skilldef.mini_icon)
    super().__init__(**kwargs)
    self.skilldef = skilldef