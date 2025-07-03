from game.ecs import Component
from game.utils import Vector
import game.components as C

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    #TODO: rename channel, because that's what it is now
    self.server = None
    self.networked_entities = {}
    self.player_entity_map = {}

  def player_register(self, client_id, entity_id):
    self.player_entity_map[client_id] = entity_id
  
  def player_unregister(self, client_id):
    del self.player_entity_map[client_id]

  def find_player_by_entity_id(self, needle):
    for client_id, entity_id in self.player_entity_map.items():
      if entity_id == needle:
        return client_id
    return None

  def network_register(self, entity):
    id = entity.get_component(C.Networking).id
    self.networked_entities[id] = entity
    #TODO: send spawned event (would require networking other components, not just actor)

  def network_unregister(self, entity):
    id = entity.get_component(C.Networking).id
    try:
      del self.networked_entities[id]
    except:
      print("[Server] ERROR: tried to delete entity that doesn't exist with id " + id)
