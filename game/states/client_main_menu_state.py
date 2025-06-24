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
        #TODO: submenu for join game
        ("Join Game", lambda _: self.game.join_game()),
        ("Create Game", lambda _: self.game.create_game()),
        ("Play Offline", lambda _: self.game.play_offline()),
        ("Settings", lambda _: None)
      ])
    ])

    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])

  def step(self, pressed, held, released, unicode_pressed):
    #control player (and other keyhandlers like menus)
    for key_handler in self.world.find_components(C.KeyHandler):
      key_handler.handle_keys(pressed, held, released, unicode_pressed)

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)