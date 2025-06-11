from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C

@dataclass
class EmitterUpdated:
  id: str
  particle_path: str
  min_vel: float
  max_vel: float
  per_tick: int
  particle_life: float
  time: float

class EmitterUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(EmitterUpdated)

  def handle(self, client_manager, client, event):
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
