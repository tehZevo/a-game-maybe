import pygame

from game.ecs import Component
from .drawable import Drawable

from ..physics.position import Position
from game.constants import DT
from game.utils.image_cache import get_image
from game.utils import Vector
import game.components as C
from game.graphics import DamageNumberType, damage_number_color

#TODO: constants
SEPARATION = 6 / 16
STACK_SEPARATION = 12 / 16 #TODO: hardcoded tile size division
DAMAGE_NUMBER_TIME = 1
DAMAGE_NUMBER_HEIGHT = 1

class DamageNumber(Component, Drawable):
  def __init__(self, number, damage_type=DamageNumberType.NORMAL, stack=0, delay=0):
    super().__init__()
    self.number = str(int(number))
    self.delay = delay
    self.stack = stack
    self.damage_type = damage_type
    self.time = 0
    self.require(C.Position)
    
    self.images = []
    self.requirements = [Position]
    self.sound_played = False
    self.start_pos = None
  
  def start(self):
    #TODO: handle k/m/b/t
    self.images = [get_image(f"assets/ui/numbers/{n}.png") for n in self.number]
    self.start_pos = self.get_component(C.Position).pos

  def update(self):
    #update delay
    self.delay -= DT
    if self.delay > 0:
      return

    self.time += DT
    
    #update position
    pos_comp = self.get_component(C.Position)
    pos_comp.pos = self.start_pos + Vector(0, self.time / DAMAGE_NUMBER_TIME * -DAMAGE_NUMBER_HEIGHT)

    #TODO: fade out for last N seconds
    if self.time >= DAMAGE_NUMBER_TIME:
      self.entity.remove()
      
  def draw(self, renderer):
    if self.delay >= 0:
      return
        
    pos = self.get_component(Position).pos
    color = damage_number_color(self.damage_type)

    for x, image in reversed(list(enumerate(self.images))):
      px = pos.x + x * SEPARATION - len(self.images) / 2 * SEPARATION
      py = pos.y - self.stack * STACK_SEPARATION
      renderer.draw(image, Vector(px, py), alpha=(1 - self.time / DAMAGE_NUMBER_TIME), tint=color)
