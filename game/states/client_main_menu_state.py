from game.ecs import World
import game.components as C
import game.networking.events as E
import game.networking.commands as commands
from game.utils import Vector

class ClientMainMenuState:
  def __init__(self, game):
    self.game = game
    
    self.world = World()
    self.ui_manager = C.UIManager()
    self.world.create_entity([self.ui_manager])

    join_code_screen = C.JoinCodeScreen(self.game)

    self.ui_manager.open_menu([
      ("Join Game", lambda _: self.ui_manager.open_screen(join_code_screen)),
      ("Create Game", lambda _: self.game.create_game()),
      ("Play Offline", lambda _: self.game.play_offline()),
      ("Settings", lambda _: None)
    ], pos=Vector(32, 32))

    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])

  def step(self, keyboard):
    self.ui_manager.handle_keys(keyboard)

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)