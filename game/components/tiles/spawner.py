import random

from game.ecs import Component, Entity
from game.utils import Vector
from game.utils.constants import DT
from ..physics import Position
from . import TileEntity

class Spawner(TileEntity):
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
    #choose random position around spawner
    spawn_pos = self.get_component(Position).pos + Vector.random() * random.random() * self.radius
    #spawn entity
    entity = self.entity.world.create_entity([
      Position(spawn_pos),
      self.component_type()
    ])
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
