from collections import defaultdict

import pygame

class Keyboard:
  def __init__(self, events):
    self.pressed = defaultdict(lambda: False)
    self.released = defaultdict(lambda: False)
    self.unicode = None
    for event in events:
      if event.type == pygame.KEYDOWN:
        self.pressed[event.key] = True
        self.unicode = event.unicode
      if event.type == pygame.KEYUP:
        self.released[event.key] = True
    self.held = pygame.key.get_pressed()