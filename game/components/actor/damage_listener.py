
class DamageListener:
  def __init__(self):
    pass

  def on_damage(self, attacker, amount):
    raise NotImplementedError
