
class Savable:
  def __init__(self):
    self.require(Id)

  def save_keys(self):
    raise NotImplementedError

  def save(self):
    return {k: self.__dict__[k] for k in self.save_keys()}

  def load(self, data):
    self.__dict__.update(data)
