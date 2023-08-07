import pygame

from ecs import Component
from components import Actor, Stats, Enemy, Sprite
from actions import Move, UseSkill, Pickup
from skills import CircleTarget, Damage
from utils import Vector

#TODO: hardcoded skill
SKILL = CircleTarget(component_target=Enemy, radius=5, children=[
  Damage(100)
])

class Player(Component):
  def __init__(self):
    super().__init__()
    self.require(Actor)

  def start(self):
    #TODO: hack for making enemy slower than player
    self.get_component(Stats).move_speed = 100
    self.get_component(Sprite).set_sprite("assets/player.png")

  def handle_keys(self, keys):
    if keys[pygame.K_a]:
      self.get_component(Actor).act(UseSkill(SKILL))

    if keys[pygame.K_SPACE]:
      self.get_component(Actor).act(Pickup())

    #create move dir from key status
    move_dir = Vector(
      keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
      keys[pygame.K_DOWN] - keys[pygame.K_UP]
    )

    #apply move action
    self.get_component(Actor).act(Move(move_dir))
