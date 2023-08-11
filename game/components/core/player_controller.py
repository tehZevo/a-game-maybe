import pygame

from game.ecs import Component
from game.utils import Vector

#client side controller, takes keyboard events, sends commands n stuff
class PlayerController(Component):
  def __init__(self):
    super().__init__()
    self.client = None

  def start(self):
    #TODO: circular import
    from game.components.networking import ClientManager
    self.client = self.entity.world.find_components(ClientManager)[0].client

  def handle_keys(self, keys):
    #TODO: circular import
    from game.networking.commands import PlayerMove
    #TODO: skill use
    if keys[pygame.K_a]:
      #self.get_component(Actor).act(UseSkill(test_player_skill))
      pass
    if keys[pygame.K_s]:
      #self.get_component(Actor).act(UseSkill(hax_heal))
      pass

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
