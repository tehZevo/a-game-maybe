import random

from game.ecs import Component
from game.utils import Vector
import game.components as C
from .particle import Particle
from game.constants import DT
from game.components.networking.network_behavior import NetworkBehavior

#TODO: more emitter styles
#TODO: particle def?
#TODO: then how to parameterize? might as well make a createemitter event
#serverside emitter just tells the client to create an emitter and then dies
#client side emitter runs until finished, then dies
#TODO: support fractional per tick (random or count ticks?)
#TODO: rotation (0/90/180/270/random)
#TODO: anim_dir: forward/reverse/random
#TODO: loop
#TODO: some kind of animation speed to use with loop vs time
class ParticleEmitter(Component, NetworkBehavior):
  def __init__(self, particle_path=None, min_vel=2, max_vel=3, per_tick=10, flip="none", particle_life=0.25, time=0):
    super().__init__()
    self.require(C.Position, C.Networking, C.PositionSyncing, C.VelocitySyncing)
    self.particle_path = particle_path
    self.system = None
    self.time = time
    self.min_vel = min_vel
    self.max_vel = max_vel
    self.per_tick = per_tick
    self.particle_life = particle_life
    self.flip = flip
    self.active = False

  def start_server(self, networking):
    from game.networking.events import ParticleEmitterUpdated
    networking.broadcast_synced(ParticleEmitterUpdated(
      id=networking.id,
      particle_path=self.particle_path,
      min_vel=self.min_vel,
      max_vel=self.max_vel,
      per_tick=self.per_tick,
      particle_life=self.particle_life,
      time=self.time,
      flip=self.flip
    ))
    
  def start_client(self, networking):
    self.system = self.entity.world.find_component(C.ParticleSystem)
  
  def update_server(self, networking):
    self.time -= DT
    if self.time <= 0:
      self.entity.alive = False
      
  def update_client(self, networking):
    if self.time < 0:
      return
      
    #TODO: kinda janky -- wait for particle path to be set by EmitterUpdated before acting
    #TODO: set an active flag when we receive the event
    if self.particle_path == None:
      return

    pos = self.entity[C.Position].pos.copy()

    #add some particles
    for _ in range(self.per_tick):
      dir = Vector.random()
      speed = self.min_vel + random.random() * (self.max_vel - self.min_vel)
      vel = dir * speed
      if self.flip == "random":
        flip = random.choice(["none", "x", "y", "both"])
      else:
        flip = self.flip
      self.system.add(Particle(
        path=self.particle_path,
        pos=pos,
        vel=vel,
        life=self.particle_life,
        flip=flip,
      ))

    self.time -= DT

  def emit(self, particle):
    self.system.add_particle(particle)
