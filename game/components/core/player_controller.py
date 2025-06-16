import pygame

from game.ecs import Component
from game.utils import Vector
from game.utils import find_entity_by_id
from game.items.slots import SkillSlot

#client side controller, takes keyboard events, sends commands n stuff
class PlayerController(Component):
  def __init__(self, id):
    super().__init__()
    self.id = id
    self.client = None
    self.player = None
    self.previous_move_dir = None

  def start(self):
    from game.components.networking import ClientManager
    self.client = self.entity.world.find_component(ClientManager).client
    self.player = find_entity_by_id(self.entity.world, self.id)

  def handle_keys(self, pressed, held, released):
    from game.networking.commands import PlayerMove, PlayerUseSkill, PlayerInteract

    #TODO: make it so you have to press
    skill = None
    if pressed[pygame.K_a]:
      skill = SkillSlot.ALPHA
    elif pressed[pygame.K_s]:
      skill = SkillSlot.BETA
    elif pressed[pygame.K_d]:
      skill = SkillSlot.GAMMA
    elif pressed[pygame.K_f]:
      skill = SkillSlot.DELTA
    elif pressed[pygame.K_q]:
      skill = SkillSlot.OMEGA
    elif pressed[pygame.K_SPACE]:
      self.client.send(PlayerInteract())
      self.previous_move_dir = None
    
    if skill is not None:
      self.client.send(PlayerUseSkill(skill))
      self.previous_move_dir = None

    #create move dir from key status
    move_dir = Vector(
      held[pygame.K_RIGHT] - held[pygame.K_LEFT],
      held[pygame.K_DOWN] - held[pygame.K_UP]
    )

    if move_dir != self.previous_move_dir:
      self.client.send(PlayerMove(move_dir))
      self.previous_move_dir = move_dir
