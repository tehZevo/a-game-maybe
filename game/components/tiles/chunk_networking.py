import math
import itertools

from game.ecs import Component
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior
from game.utils.constants import CHUNK_SIZE
import game.networking.events as E

def overlap(old_chunk, new_chunk):
  nx, ny = new_chunk
  new = set(itertools.product([nx-1, nx, nx+1], [ny-1, ny, ny+1]))
  
  if old_chunk is None:
    return list(new), []

  ox, oy = old_chunk
  old = set(itertools.product([ox-1, ox, ox+1], [oy-1, oy, oy+1]))

  return list(new - old), list(old - new)

#TODO: this is spawned on client due to networkbehavior.. need a flag or separate component that controls spawning on client
class ChunkNetworking(Component, NetworkBehavior):
  def __init__(self, chunks=None):
    super().__init__()
    self.chunks = chunks
    self.player_chunk_pos = {}
    self.require(C.Networking)
  
  def get_player_events(self, client_id, new_chunk):
    if self.player_chunk_pos.get(client_id) == new_chunk:
      return []
    
    player_events = []
    old_chunk = self.player_chunk_pos.get(client_id)
    to_load, to_unload = overlap(old_chunk, new_chunk)
    for (cx, cy) in to_load:
      if (cx, cy) not in self.chunks:
        continue
      player_events.append(E.ChunkLoaded(cx, cy, self.chunks[(cx, cy)].pack()))
    for (cx, cy) in to_unload:
      if (cx, cy) not in self.chunks:
        continue
      player_events.append(E.ChunkUnloaded(cx, cy))
    return player_events
  
  def update_server(self, networking):
    players = networking.server_manager.player_entity_map
    for client_id, entity_id in players.items():
      entity = networking.server_manager.networked_entities[entity_id]
      pos = entity.get_component(C.Position).pos
      new_chunk = (math.floor(pos.x / CHUNK_SIZE), math.floor(pos.y / CHUNK_SIZE))
      evts = self.get_player_events(client_id, new_chunk)
      for evt in evts:
        networking.send_to_client(client_id, evt)
      self.player_chunk_pos[client_id] = new_chunk
