
#TODO: sequential, parallel, delay
#TODO: offset effect or some way to disjoint a target

class SkillEffect:
  def __init__(self):
    self.completed = True
    self.entity = None
    self.target = None
    self.children = []

  def register(self, entity):
    self.entity = entity

  def start(self):
    pass

  def update(self):
    pass
