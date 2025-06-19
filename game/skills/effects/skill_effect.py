
#TODO: sequential, parallel, delay
#TODO: offset based on actor look direction
#TODO: delay chain (provide sequence of skill effects)
#TODO: repeat
#TODO: "homing" - has speed/lerp, moves towards target and doesn't activate until it's within a certain distance

class SkillEffect:
  def __init__(self):
    pass

  def start(self, skill):
    """Optionally return a state value/object"""
    return None

  def update(self, skill, state):
    """Optionally return a state value/object"""
    return state

  def remove(self, skill, state):
    pass
