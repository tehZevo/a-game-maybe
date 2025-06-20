from game.ecs import Component
from game.items.defs import SkillItem
import game.data.skills as S
import game.data.sprites as Sprites
from .damage_listener import DamageListener
from .death_listener import DeathListener
from game.utils.teams import PLAYER
from game.utils.constants import PLAYER_INVULN_TIME
import game.components as C
from game.utils import Vector
from game.utils.constants import PLAYER_MOVE_SPEED

class Player(Component, DamageListener, DeathListener):
  def __init__(self):
    super().__init__()
    self.require(C.Actor)
    self.ghost = None

  def start(self):
    self.get_component(C.Stats).move_speed_multiplier = PLAYER_MOVE_SPEED
    sprite = self.get_component(C.Sprite)
    sprite.set_sprite(Sprites.player)
    sprite.set_animation("idle") #TODO: maybe need a string enum for actor/player animations
    self.get_component(C.Team).team = PLAYER
    equips = self.get_component(C.Equips)
    #TODO: this should probably be save data, but we would need to inject it in the connect handler?
    equips.equip(SkillItem(S.test_player_skill))
    equips.equip(SkillItem(S.hax_heal))
    equips.equip(SkillItem(S.test_buff_skill))
    equips.equip(SkillItem(S.test_killme_skill))

  def on_damage(self, attacker, amount):
    if self.get_component(C.Invulnerable) is None:
      self.entity.add_component(C.Invulnerable(PLAYER_INVULN_TIME))
  
  def update(self):
    actor = self.get_component(C.Actor)
    sprite = self.get_component(C.Sprite)
    pos = self.get_component(C.Position)
    if self.ghost is None and not actor.actor_alive and sprite.animation_finished:
      self.ghost = self.entity.world.create_entity([
        C.Position(pos.pos.copy() + Vector(0.5, -1)),
        C.Ghost(),
      ])

  def on_death(self):
    sprite = self.get_component(C.Sprite)
    sprite.set_sprite(Sprites.tombstone)
    sprite.set_speed(4)