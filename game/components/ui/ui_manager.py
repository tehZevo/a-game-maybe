import pygame

from game.ecs import Component
import game.components as C
from game.utils.image_cache import get_image

from game.utils import Vector
from game.components.core import KeyHandler
from game.utils import image_utils

class UIManager(Component, KeyHandler):
  def __init__(self, options=[], selection=0):
    super().__init__()
    self.focus_stack = []
  
  def handle_keys(self, kbd):
    if len(self.focus_stack) > 0 and kbd.pressed[pygame.K_ESCAPE]:
      self.pop()
    
    if len(self.focus_stack) == 0:
      return
    
    self.focus_stack[-1].handle_keys(kbd)
  
  def pop(self):
    self.focus_stack.pop()
  
  def push(self, c):
    self.focus_stack.append(c)
  
  def open_screen(self, screen):
    self.push(screen)
    self.entity.world.create_entity([screen])
  
  def open_menu(self, menu_items, pos=None, selection=0):
    pos = pos or Vector()
    menu = C.Menu(menu_items, selection)
    self.push(menu)
    self.entity.world.create_entity([
      C.Position(pos),
      menu
    ])
