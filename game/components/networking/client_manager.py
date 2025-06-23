from game.ecs import Component

import game.components as C

class ClientManager(Component):
  def __init__(self):
    super().__init__()
    #TODO: rename to channel
    self.client = None
    self.networked_entities = {}

  def network_register(self, entity):
    id = entity.get_component(C.Networking).id
    self.networked_entities[id] = entity

  def network_unregister(self, id):
    ent = self.networked_entities[id]
    del self.networked_entities[id]
    return ent
