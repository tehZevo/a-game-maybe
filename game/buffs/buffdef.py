
#TODO: cancel behavior (always override, override if higher, never override?)
#TODO: max_power, max_stacks, max_time etc?

class BuffDef:
  def __init__(self, id, effects, icon=None):
    self.id = id
    self.effects = effects
    self.icon = icon
