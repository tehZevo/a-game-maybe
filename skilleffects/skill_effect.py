
#TODO: sequential, parallel, delay
#TODO: offset effect or some way to disjoint a target

class SkillEffect:
  def __init__(self):
    self.completed = True
    self.entity = None
    self.user = None
    self.target = None
    self.children = []

  def register(self, entity, user):
    self.entity = entity
    self.user = user

  def start(self):
    pass

  def update(self):
    pass
