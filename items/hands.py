from items import Weapon

#a "dummy" weapon for when you have no weapon equipped
class Hands(Weapon):
  def __init__(self):
    super().__init__()
