import random

from pygame.math import Vector2

from game.ecs import Component
from game.particles.particle import Particle
from game.utils import Vector
import game.components as C
from . import ParticleSystem
from game.utils.constants import DT

#TODO: more emitter styles
class ParticleEmitter(Component):
  def __init__(self, particle_path, min_vel=2, max_vel=3, per_tick=10, particle_life=0.25, time=0):
    super().__init__()
    self.require(C.Position)
    self.particle_path = particle_path
    self.system = None
    self.time = time
    self.min_vel = min_vel
    self.max_vel = max_vel
    self.per_tick = per_tick
    self.particle_life = particle_life

  def start(self):
    #TODO: network (may require dataclassing particle emitter and particle)
    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    from ..networking import ClientManager
    if not self.entity.world.find_component(ClientManager):
      self.is_server = True
      return

    self.system = self.entity.world.find(ParticleSystem)[0]
    self.system = self.system.get_component(ParticleSystem)

  def update(self):
    if self.is_server:
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
