
class Interactable:
  def __init__(self):
    pass

  #entity = the actor that is interacting
  def interact(self, entity):
    raise NotImplementedError
