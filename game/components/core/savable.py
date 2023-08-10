
class Savable:
  def __init__(self):
    self.require(Id)

  def save(self):
    raise NotImplementedError

  def load(self, data):
    self.__dict__.update(data)
