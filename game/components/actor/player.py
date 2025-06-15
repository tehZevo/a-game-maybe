import pygame

from game.ecs import Component
from game.actions import Move, UseSkill, Interact
from game.items.defs import SkillItem
import game.data.skills as S
import game.data.sprites as Sprites
from .damage_listener import DamageListener
from game.utils import Vector
from game.utils.teams import PLAYER
from game.utils.constants import PLAYER_INVULN_TIME
import game.components as C

class Player(Component, DamageListener):
  def __init__(self):
    super().__init__()
    self.require(C.Actor)

  def start(self):
    sprite = self.get_component(C.Sprite)
    sprite.set_sprite(Sprites.player)
    sprite.set_animation("idle") #TODO: maybe need a string enum for actor/player animations
    self.get_component(C.Team).team = PLAYER
    equips = self.get_component(C.Equips)
    #TODO: this should probably be save data, but we would need to inject it in the connect handler?
    equips.equip(SkillItem(S.test_player_skill))
    equips.equip(SkillItem(S.hax_heal))

  def on_damage(self, attacker):
    if self.get_component(C.Invulnerable) is None:
      self.entity.add_component(C.Invulnerable(PLAYER_INVULN_TIME))