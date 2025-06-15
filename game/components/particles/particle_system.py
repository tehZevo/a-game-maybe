import pygame

from game.ecs import Component

class ParticleSystem(Component):
  def __init__(self):
    super().__init__()
    self.particles = pygame.sprite.Group()

  def add_particle(self, particle):
    #using a group to track particles but not for drawing
    self.particles.add(particle)

  def update(self):
    self.particles.update()

  def draw(self, renderer):
    for particle in self.particles:
      particle.draw(renderer)
