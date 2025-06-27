import game.components as C
from .skill_effect import SkillEffect
from game.constants import DT
from game.skills.target_filters import target_type_filter, distance_filter, ignore_entities_filter
from game.skills.effects.target import apply_target
import game.data.sprites as S

class Projectile(SkillEffect):
  def __init__(self, target_type, sprite=None, on_tick=[], on_end=[], life=1, radius=1, speed=4, max_entities_hit=1):
    super().__init__()
    self.target_type = target_type
    self.on_tick = on_tick
    self.on_end = on_end
    self.life = life
    self.speed = speed
    self.radius = radius
    self.sprite = sprite

  def start(self, skill):
    skill.completed = False
    dir = skill.user[C.Actor].move_dir
    
    if self.sprite is not None:
      #babysit the sprite synced on the client
      sprite = skill.entity.world.create_entity([
        C.Position(skill.entity[C.Position].pos.copy()),
        C.Physics(),
        C.PositionSyncing(),
        C.VelocitySyncing(),
        C.Sprite(self.sprite),
        C.SpriteSyncing(),
      ])
      sprite[C.Physics].vel = dir * self.speed
      sprite[C.Physics].friction = 0 #TODO: sync friction?
    else:
      sprite = None
    return ([], self.life, dir, sprite)
  
  def update(self, skill, state):
    ents_hit, life, dir, sprite = state

    pos = skill.entity[C.Position].pos
    pos = pos + dir * self.speed * DT
    skill.entity[C.Position].pos = pos

    #TODO: consider max_entities_hit

    #basically a target effect
    filters = [
      ignore_entities_filter(ents_hit),
      distance_filter(self.radius),
      target_type_filter(self.target_type)
    ]

    new_ents_hit = apply_target(skill, filters, self.on_tick)
    ents_hit = ents_hit + new_ents_hit

    life -= DT
    if life <= 0:
      skill.completed = True
    
    return ents_hit, life, dir, sprite
    
  def remove(self, skill, state):
    ents_hit, life, dir, sprite = state

    for child in self.on_end:
      skill.entity.world.create_entity([
        C.Position(skill.entity[C.Position].pos),
        C.Skill(child, skill.user, skill.entity)
      ])
    
    if sprite is not None:
      sprite.remove()