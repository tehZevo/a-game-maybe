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
    self.ready_players = set()

    self.channel.setup_handlers([
      E.LobbyUpdatedHandler(self)
    ])

    self.world = World()
    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])

    self.ui_manager = C.UIManager()
    self.world.create_entity([self.ui_manager])

    # self.ui_manager.open_screen(C.LobbyScreen(self))
    self.ui_manager.open_screen(C.CharacterCreationScreen(self))
    
    print("[Client] Hello lobby state")

    #TODO: send hello lobby and await lobbystateupdated
    if auto_ready:
      print("[Client] Join code is", join_code, "but we don't care, starting game...")
      self.channel.send(commands.PlayerReady())
    
  def step(self, keyboard):
    self.channel.handle_events()

    #control player (and other keyhandlers like menus)
    self.ui_manager.handle_keys(keyboard)
    
    if pygame.K_RETURN in keyboard.pressed:
      print("[Client] Sending ready!")
      self.channel.send(commands.PlayerReady())

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)
