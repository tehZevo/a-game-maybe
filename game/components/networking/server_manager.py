from game.ecs import Component
from game.utils import Vector
import game.components as C

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None
    self.networked_entities = {}
    self.player_entity_map = {}

  def player_register(self, client_id, entity_id):
    self.player_entity_map[client_id] = entity_id
  
  def player_unregister(self, client_id):
    del self.player_entity_map[client_id]

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
