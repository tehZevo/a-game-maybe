
class World:
  def __init__(self):
    self.entities = []

  def add_entity(self, entity):
    self.entities.append(entity)

  def remove_entity(self, entity):
    #TODO: will this cause iteration issues? might need dead flag
    self.entities.remove(entity)

  def update(self):
    for e in self.entities:
      e.update()
