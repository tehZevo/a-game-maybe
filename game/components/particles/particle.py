import pygame

from game.constants import DT
from game.utils.image_cache import get_image
from game.utils import image_utils

#TODO: tintable particles
#TODO: homing particles (would be hard to network)
#TODO: particle swirls (circle around, swirl out, etc)
#TODO: scale particles
#TODO: rotate particles
#TODO: friction
#TODO: fading

#TODO: handle looping (or not)

#NOTE: particles are assumed to be square
class Particle:
  def __init__(self, path, pos, vel=None, life=1, flip="none"):
    super().__init__()
    self.image = get_image(path)
    self.pos = pos
    self.vel = vel or Vector2(0, 0)
    self.starting_life = life
    self.life = life
    self.flip = flip

  def update(self):
    self.pos = self.pos + self.vel * DT
    self.life -= DT

  def draw(self, renderer):
    t = 1 - self.life / self.starting_life
    #TODO: forced clamp
    frame = image_utils.get_frame_t(self.image, self.image.get_height(), t, clamp=True)
    #TODO: do this without creating a new surface?
    flip_x = self.flip == "x" or self.flip == "both"
    flip_y = self.flip == "y" or self.flip == "both"
    if flip_x or flip_y:
      # print(flip_x, flip_y)
      frame = pygame.transform.flip(frame, flip_x, flip_y)
    renderer.draw(frame, self.pos)
