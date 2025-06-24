import pygame

class KeyHandler:
  def __init__(self):
    super().__init__()

  def handle_keys(self, pressed, held, released, pressed_unicode):
    raise NotImplementedError