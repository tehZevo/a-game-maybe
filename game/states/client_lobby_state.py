import pygame

from game.ecs import World
import game.components as C
import game.networking.commands as commands
import game.networking.events as E
from game.utils import Vector

class ClientLobbyState:
  def __init__(self, game, channel, join_code, auto_ready=False):
    self.game = game
    self.channel = channel
    self.join_code = join_code

    self.channel.setup_handlers([
      #TODO
    ])

    self.world = World()
    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])
    
    print("[Client] Hello lobby state")

    #TODO: send hello lobby and await lobbystateupdated
    if auto_ready:
      print("[Client] Join code is", join_code, "but we don't care, starting game...")
      self.channel.send(commands.PlayerReady())
    
  def step(self, keyboard):
    self.channel.handle_events()

    #control player (and other keyhandlers like menus)
    for key_handler in self.world.find_components(C.KeyHandler):
      key_handler.handle_keys(keyboard)
    
    if pygame.K_RETURN in keyboard.pressed:
      print("[Client] Sending ready!")
      self.channel.send(commands.PlayerReady())

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)
