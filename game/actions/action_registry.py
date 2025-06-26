def get_action_classes():
  from .interact import Interact
  from .move import Move
  from .use_skill import UseSkill

  return locals()
