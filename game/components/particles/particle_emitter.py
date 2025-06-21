import random

from pygame.math import Vector2

from game.ecs import Component
from game.particles.particle import Particle
from game.utils import Vector
import game.components as C
from . import ParticleSystem
from game.constants import DT
from game.components.networking.network_behavior import NetworkBehavior

#TODO: more emitter styles
class ParticleEmitter(Component, NetworkBehavior):
  def __init__(self, particle_path=None, min_vel=2, max_vel=3, per_tick=10, particle_life=0.25, time=0):
    super().__init__()
    self.require(C.Position, C.Networking, C.PositionSyncing, C.VelocitySyncing)
    self.particle_path = particle_path
    self.system = None
    self.time = time
    self.min_vel = min_vel
    self.max_vel = max_vel
    self.per_tick = per_tick
    self.particle_life = particle_life

  def start_server(self, networking):
    from game.networking.events import EmitterUpdated
    networking.broadcast_synced(EmitterUpdated(
      id=networking.id,
      particle_path=self.particle_path,
      min_vel=self.min_vel,
      max_vel=self.max_vel,
      per_tick=self.per_tick,
      particle_life=self.particle_life,
      time=self.time
    ))
    #TODO: how to know when to remove particle emitter?
    #TODO: do we need a "desync" so the client doesn't despawn?
    #TODO: or would it be a flag on networkbehavior?
    self.entity.remove() #?? why no work?
    print(len(self.entity.world.entities))

  def start_client(self, networking):
    self.system = self.entity.world.find(ParticleSystem)[0]
    self.system = self.system.get_component(ParticleSystem)

  def update_client(self, networking):
    #TODO: kinda janky -- wait for particle path to be set by EmitterUpdated before acting
    if self.particle_path == None:
      return

    pos = Vector2(*self.entity.get_component(C.Position).pos.tolist())

    #add some particles
    for _ in range(self.per_tick):
      dir = Vector2(*Vector.random().tolist())
      speed = self.min_vel + random.random() * (self.max_vel - self.min_vel)
      vel = dir * speed
      self.system.add_particle(Particle(
        path=self.particle_path,
        pos=pos,
        vel=vel,
        life=self.particle_life
      ))

    self.time -= DT
    if self.time <= 0:
      self.entity.alive = False

  def emit(self, particle):
    self.system.add_particle(particle)
