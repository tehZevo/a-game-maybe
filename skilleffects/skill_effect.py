
#TODO: sequential, parallel, delay
#TODO: offset effect or some way to disjoint a target

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
