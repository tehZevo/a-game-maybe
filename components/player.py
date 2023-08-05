import pygame

from ecs import Component
from components import Actor, Stats
from actions import Move
from utils import Vector

class Player(Component):
  def __init__(self):
    super().__init__()
    self.require(Actor)

  def init(self):
    #TODO: hack for making enemy slower than player
    self.get_component(Stats).move_speed = 100

  def handle_keys(self, keys):
    #create move dir from key status
    move_dir = Vector(
      keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
      keys[pygame.K_DOWN] - keys[pygame.K_UP]
    )

    #apply move action
    self.get_component(Actor).act(Move(move_dir))
