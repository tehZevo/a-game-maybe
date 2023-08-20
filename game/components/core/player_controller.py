import pygame

from game.ecs import Component
from game.utils import Vector
from game.utils import find_entity_by_id
from game.items import SkillSlot

#client side controller, takes keyboard events, sends commands n stuff
class PlayerController(Component):
  def __init__(self, id):
    super().__init__()
    self.id = id
    self.client = None
    self.player = None

  def start(self):
    #TODO: circular import
    from game.components.networking import ClientManager
    self.client = self.entity.world.find_components(ClientManager)[0].client
    self.player = find_entity_by_id(self.entity.world, self.id)

  def handle_keys(self, keys):
    #TODO: circular import
    from game.networking.commands import PlayerMove, PlayerUseSkill
    #TODO: skill use
    if keys[pygame.K_a]:
      self.client.send(PlayerUseSkill(SkillSlot.ALPHA))
    if keys[pygame.K_s]:
      self.client.send(PlayerUseSkill(SkillSlot.BETA))
    if keys[pygame.K_d]:
      self.client.send(PlayerUseSkill(SkillSlot.GAMMA))
    if keys[pygame.K_f]:
      self.client.send(PlayerUseSkill(SkillSlot.DELTA))
    if keys[pygame.K_q]:
      self.client.send(PlayerUseSkill(SkillSlot.OMEGA))

    #TODO: interact use
    if keys[pygame.K_SPACE]:
      # self.get_component(Actor).act(Interact())
      pass

    #create move dir from key status
    move_dir = Vector(
      keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
      keys[pygame.K_DOWN] - keys[pygame.K_UP]
    )

    if move_dir != Vector.ZERO:
      #send move command
      self.client.send(PlayerMove(move_dir))
