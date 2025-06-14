from game.ecs import Component
from game.utils import Vector
from game.utils.constants import DT, PHYS_SCALE
from game.components.physics import Position, Collisions, Rect

DEFAULT_MASS = 1
DEFAULT_FRICTION = 0.5

def collision_test(a, rects):
  return [b for b in rects if a.colliderect(b)]

#TODO: could really use a basic vector class
class Physics(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.mass = DEFAULT_MASS
    self.friction = DEFAULT_FRICTION
    self.force = Vector()
    self.vel = Vector()
    self.is_server = False

  def apply_force(self, force):
    self.force = self.force + force

  def start(self):
    import game.components as C
    #TODO: hmm this is n squared, caching in start for now
    self.tile_phys = self.entity.world.find_component(C.TilePhysics)
    self.is_server = self.entity.world.find_component(C.ServerManager) is not None

  def update(self):
    #TODO: for now, no physics on client
    if not self.is_server:
      return
    
    pc = self.get_component(Position)
    handle_collisions = self.get_component(Collisions) is not None
    rect = self.get_component(Rect) if handle_collisions else None

    if handle_collisions:
      tile_rects = self.tile_phys.get_rects_for_pos(pc.pos)
    
    #two-phase physics for sliding collisions
    self.vel.x = self.vel.x + self.force.x / self.mass * DT
    dx = self.vel.x * DT
    pc.pos.x = pc.pos.x + dx

    if handle_collisions:
      #update rect (TODO: this is so messy)
      rect.update()
      collisions = collision_test(rect.rect, tile_rects)
      for other_rect in collisions:
        if dx > 0:
          rect.rect.right = other_rect.left
          self.vel.x = 0
        elif dx < 0:
          rect.rect.left = other_rect.right
          self.vel.x = 0

      #sync to rect pos
      pc.pos.x = rect.rect.left / PHYS_SCALE
      #update rect AGAIN (TODO: this is so messy)
      rect.update()

    self.vel.y = self.vel.y + self.force.y / self.mass * DT
    dy = self.vel.y * DT
    pc.pos.y = pc.pos.y + dy

    if handle_collisions:
      #update rect (TODO: this is so messy)
      rect.update()
      collisions = collision_test(rect.rect, tile_rects)
      for other_rect in collisions:
        if dy > 0:
          rect.rect.bottom = other_rect.top
          self.vel.y = 0
        elif dy < 0:
          rect.rect.top = other_rect.bottom
          self.vel.y = 0

      #sync to rect pos
      pc.pos.y = rect.rect.top / PHYS_SCALE
      #update rect AGAIN (TODO: this is so messy)
      rect.update()


    #reset force
    self.force = Vector()

    #apply friction
    self.vel = self.vel / (1 + self.friction)
