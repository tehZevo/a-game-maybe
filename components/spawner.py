import random

from ecs import Component, Entity
from components import Position
from utils import Vector
from utils.constants import DT

class Spawner(Component):
  #provide a type of component to spawn
  def __init__(self, component_type, wave_time=2, wave_count=3, radius=4, spawn_max=10):
    super().__init__()
    self.component_type = component_type
    self.wave_time = wave_time
    self.wave_count = wave_count
    self.radius = radius
    self.spawned = []
    self.remaining_wave_time = self.wave_time
    self.spawn_max = spawn_max

  def spawn(self):
    entity = Entity()
    entity.add_component(self.component_type())
    #assume entity has position
    #set entity's position radomly in a disc around spawner
    spawn_pos = self.get_component(Position).pos + Vector.random() * random.random() * self.radius
    entity.get_component(Position).pos = spawn_pos
    self.entity.world.add_entity(entity)
    self.spawned.append(entity)

  def spawn_wave(self):
    #spawn up to wave_count, stop when we hit the max
    for _ in range(self.wave_count):
      if len(self.spawned) >= self.spawn_max:
        break
      self.spawn()

  def update(self):
    self.remaining_wave_time -= DT
    if self.remaining_wave_time <= 0:
      self.spawn_wave()
      self.remaining_wave_time = self.wave_time

    #TODO: update removed entities
    self.spawned = [e for e in self.spawned if e.alive]
