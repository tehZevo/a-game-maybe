from dataclasses import dataclass

from game.utils import Vector
from game.networking import PlayStateEventHandler
import game.components as C

@dataclass
class ParticleEmitterUpdated:
  id: str
  particle_path: str
  min_vel: float
  max_vel: float
  per_tick: int
  particle_life: float
  time: float
  flip: str

class ParticleEmitterUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(ParticleEmitterUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    #TODO: this is caused by entities not being on client yet.. need to sync them when client first "sees" them
    # this either means sending actor spawned for all ents upon player join, OR having other actors/networked components spawn/despawn themselves on the client
    if event.id not in client_manager.networked_entities:
      print("trying to update emitter with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.networked_entities[event.id]
    if ent is not None:
      emitter = ent.get_component(C.ParticleEmitter)
      emitter.particle_path = event.particle_path
      emitter.min_vel = event.min_vel
      emitter.max_vel = event.max_vel
      emitter.per_tick = event.per_tick
      emitter.particle_life = event.particle_life
      emitter.time = event.time
      emitter.flip = event.flip
