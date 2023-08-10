
#TODO: sequential, parallel, delay
#TODO: offset based on actor look direction
#TODO: delay chain (provide sequence of skill effects)
#TODO: repeat

class SkillEffect:
  def __init__(self):
    self.completed = True
    self.entity = None
    self.user = None
    self.target = None
    self.children = []
    self.parent = None

  #TODO: i dont like this.. skill effects shouldnt store state
  def register(self, entity, user, parent=None):
    self.entity = entity
    self.user = user
    self.parent = parent

  def start(self):
    pass

  def update(self):
    pass
