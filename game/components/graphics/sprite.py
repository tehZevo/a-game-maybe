from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.constants import TILE_SIZE, DT

class Sprite(Component, Drawable):
  def __init__(self, sprite=None, animation=None):
    super().__init__()
    self.require(C.Position)
    self.sprite = sprite
    self.pos = None
    self.time = 0
    self.speed = 1
    self.animation = animation or "default" #TODO: interfaces with SimpleSprite animation "default"
    self.tint = None
    self.alpha = None
    self.offset = None
    self.flip_x = False
    #TODO: use in spritedef
    self.palette = None
    self.dirty = False

  @property
  def animation_finished(self):
    if self.sprite is None or self.animation not in self.sprite.animations:
      return False
    return not self.sprite.animations[self.animation].loop and self.time >= 1
    
  def set_sprite(self, sprite):
    self.sprite = sprite
    if "default" in sprite.animations:
      self.set_animation("default")
    else:
      #TODO: are there any cases where we need to change sprite but KEEP our current animation id?
      self.animation = None
    self.set_time(0)
    self.dirty = True
  
  def set_palette(self, palette):
    self.palette = palette
    self.dirty = True

  def set_animation(self, animation):
    if self.animation == animation or self.sprite is None:
      return
    if animation not in self.sprite.animations:
      return

    self.animation = animation
    self.set_time(0)
    self.dirty = True
  
  def set_speed(self, speed):
    if speed != self.speed:
      self.speed = speed
      self.dirty = True
  
  def set_time(self, time):
    if time != self.time:
      self.dirty = True
      self.time = time

  def start(self):
    self.pos = self.get_component(C.Position)

  def update(self):
    self.time += self.speed * DT
    
    #check for updates and notify listeners
    if self.dirty:
      for component in self.entity.components.values():
        if not isinstance(component, C.SpriteListener):
          continue
        component.on_sprite_changed(self)
      self.dirty = False

  def draw(self, renderer):
    if self.sprite is None or self.animation is None:
      return
    
    pos = self.pos.pos.copy()
    self.sprite.draw(renderer, self.tint, self.alpha, self.animation, self.time, pos, self.offset, self.flip_x)