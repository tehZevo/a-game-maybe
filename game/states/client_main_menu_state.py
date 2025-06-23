import sys
from collections import defaultdict

import pygame

from game.ecs import World
import game.components as C
import game.networking.events as E
import game.networking.commands as commands
from game.utils import Vector

class ClientMainMenuState:
  def __init__(self, game):
    self.game = game
    
    self.world = World()
    self.world.create_entity([
      C.Position(Vector(32, 32)),
      C.Menu([
        ("Singleplayer", lambda _: self.game.create_singleplayer_client()),
        ("Multiplayer", lambda _: self.game.create_multiplayer_client()),
        ("asdf", lambda _: print("asdf")),
        ("asdf", lambda _: print("asdf"))
      ])
    ])

    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])

  def step(self, pressed, held, released):
    #control player (and other keyhandlers like menus)
    for key_handler in self.world.find_components(C.KeyHandler):
      key_handler.handle_keys(pressed, held, released)

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)