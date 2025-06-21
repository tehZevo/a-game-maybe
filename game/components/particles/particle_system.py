from game.ecs import Component
from game.components.graphics import Drawable

class ParticleSystem(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.particles = []

  def add(self, particle):
    self.particles.append(particle)

  def update(self):
    for p in self.particles:
      p.update()

  def draw(self, renderer):
    for particle in self.particles:
      particle.draw(renderer)
    
    self.particles = [p for p in self.particles if p.life > 0]
