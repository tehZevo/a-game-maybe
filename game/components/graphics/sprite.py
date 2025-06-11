import pygame
from pygame import Vector2

from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.utils.constants import PPU

#TODO: animations
class Sprite(Component, Drawable):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Position)
    self.path = path
    self.surface = None
    self.pos = None

  def start(self):
    self.pos = self.get_component(C.Position)
    
    if self.path is not None:
      self.set_sprite(self.path)

  def set_sprite(self, path):
    if self.path == path:
      return

    self.path = path

    for component in self.entity.components.values():
      if not isinstance(component, C.SpriteListener):
        continue
      component.on_sprite_changed(self)

    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    #TODO: maybe move this logic to sprite networking since its behavior is different on client and server
    if not self.entity.world.find_component(C.ClientManager):
      return

    self.surface = get_image(path)

  def draw(self, screen, offset):
    if self.surface is not None:
      pos = self.pos.pos
      pos = Vector2(*(e * PPU for e in pos.tolist()))
      screen.blit(self.surface, pos + offset)