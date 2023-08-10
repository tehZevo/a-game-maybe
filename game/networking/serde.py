import json

class Serde:
  def deserialize(data, type):
    return type(json.reads(data))

  def __init__(self):
    self._type = self.__class__.__name__

  def serialize(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__)
