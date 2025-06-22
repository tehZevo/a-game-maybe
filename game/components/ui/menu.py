import pygame

from .ui_component import UIComponent
import game.components as C
from game.utils.image_cache import get_image

from game.utils import Vector
from game.components.core import KeyHandler

#TODO: move to imageutils
def text_to_surfaces(text):
  font = get_image("assets/ui/font.png")
  text = text.encode("ascii")
  surfs = []
  for c in text:
    x = (c % 16) * 8
    y = (c // 16) * 8
    surfs.append(font.subsurface((x, y, 8, 8)))
  return surfs

#TODO: make utility function
#TODO: for now, w/h are full 8x8 chunks of the 9patch
def draw_9patch(renderer, image_path, offset, w, h):
  image = get_image(image_path)
  def get_patch(x, y):
    px = 0 if x == 0 else 2 if x == w - 1 else 1
    py = 0 if y == 0 else 2 if y == h - 1 else 1
    return image.subsurface((px * 8, py * 8, 8, 8))

  for y in range(h):
    for x in range(w):
      patch = get_patch(x, y)
      renderer.draw(patch, offset + Vector(x * 8, y * 8))

def draw_text(renderer, text, offset, color=(0, 0, 0)):
  surfaces = text_to_surfaces(text)
  for i, surf in enumerate(surfaces):
    renderer.draw(surf, offset + Vector(i * 8, 0), tint=color)

class Menu(UIComponent, KeyHandler):
  def __init__(self, options=[], selection=0):
    super().__init__()
    self.options = options
    self.selection = 0
    self.max_option_length = max([len(text) for text, _ in self.options])
  
  def handle_keys(self, pressed, held, released):
    if pressed[pygame.K_DOWN]:
      self.down()
    if pressed[pygame.K_UP]:
      self.up()
    if pressed[pygame.K_SPACE]:
      self.select()
  
  def down(self):
    self.selection = max(0, min(self.selection + 1, len(self.options) - 1))
  
  def up(self):
    self.selection = max(0, min(self.selection - 1, len(self.options) - 1))
  
  def select(self):
    self.options[self.selection][1](self)
  
  def draw(self, renderer):
    pos = self.get_component(C.Position).pos #TODO: cache pos comp
    max_len = max([len(o) for o in self.options])
    draw_9patch(renderer, "assets/ui/box.png", pos, self.max_option_length + 2 + 1, len(self.options) + 2)
    for i, (text, _) in enumerate(self.options):
      spacer = ">" if i == self.selection else " "
      draw_text(renderer, spacer + text, pos + Vector(8, (i + 1) * 8))