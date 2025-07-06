import pygame

from game.ecs import Component
from .drawable import Drawable

from game.constants import DT, DAMAGE_NUMBER_SEPARATION, DAMAGE_NUMBER_HEIGHT, \
  DAMAGE_NUMBER_STACK_DELAY, DAMAGE_NUMBER_STACK_SEPARATION, DAMAGE_NUMBER_TIME
from game.utils.image_cache import get_image
from game.utils import Vector
import game.components as C
from game.graphics import DamageNumberType, damage_number_color

class DamageNumber(Component, Drawable):
  def __init__(self, number, damage_type=DamageNumberType.NORMAL, stack=0):
    super().__init__()
    self.require(C.Position)
    self.number = str(int(number))
    self.delay = stack * DAMAGE_NUMBER_STACK_DELAY
    self.stack = stack
    self.damage_type = damage_type
    self.time = 0
    
    self.images = []
    self.sound_played = False
    self.start_pos = None
  
  def start(self):
    #TODO: handle k/m/b/t
    self.images = [get_image(f"assets/ui/numbers/{n}.png") for n in self.number]
    self.start_pos = self.entity[C.Position].pos

  def update(self):
    #update delay
    self.delay -= DT
    if self.delay > 0:
      return

    self.time += DT
    
    #update position
    pos_comp = self.entity[C.Position]
    pos_comp.pos = self.start_pos + Vector(0, self.time / DAMAGE_NUMBER_TIME * -DAMAGE_NUMBER_HEIGHT)

    if self.time >= DAMAGE_NUMBER_TIME:
      self.entity.remove()
      
  def draw(self, renderer):
    if self.delay >= 0:
      return
        
    pos = self.entity[C.Position].pos
    color = damage_number_color(self.damage_type)

    for x, image in reversed(list(enumerate(self.images))):
      px = pos.x + x * DAMAGE_NUMBER_SEPARATION - len(self.images) / 2 * DAMAGE_NUMBER_SEPARATION
      py = pos.y - self.stack * DAMAGE_NUMBER_STACK_SEPARATION
      renderer.draw(image, Vector(px, py), alpha=(1 - self.time / DAMAGE_NUMBER_TIME), tint=color)
