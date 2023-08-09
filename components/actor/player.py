import pygame

from ecs import Component
from components.actor.actor import Actor
from components.graphics.sprite import Sprite
from .invulnerable import Invulnerable
from .damage_listener import DamageListener
from actions import Move, UseSkill, Interact
from utils import Vector

from skills.test_player_skill import test_player_skill

PLAYER_INVULN_TIME = 1 #seconds

class Player(Component, DamageListener):
  def __init__(self):
    super().__init__()
    self.require(Actor)

  def start(self):
    self.get_component(Sprite).set_sprite("assets/player.png")

  def on_damage(self, attacker):
    if self.get_component(Invulnerable) is None:
      self.entity.add_component(Invulnerable(PLAYER_INVULN_TIME))

  def handle_keys(self, keys):
    if keys[pygame.K_a]:
      self.get_component(Actor).act(UseSkill(test_player_skill))

    if keys[pygame.K_SPACE]:
      self.get_component(Actor).act(Interact())

    #create move dir from key status
    move_dir = Vector(
      keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
      keys[pygame.K_DOWN] - keys[pygame.K_UP]
    )

    if move_dir != Vector.ZERO:
      #apply move action
      self.get_component(Actor).act(Move(move_dir))
