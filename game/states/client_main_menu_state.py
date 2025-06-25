from game.ecs import World
import game.components as C
import game.networking.events as E
import game.networking.commands as commands
from game.utils import Vector

def make_server_url_screen(game):
  current_server_url = game.config.server_url
  return C.TextInputScreen(
    lambda url: game.config.set_server_url(url),
    default_text=current_server_url
  )

class ClientMainMenuState:
  def __init__(self, game):
    self.game = game
    
    self.world = World()
    self.ui_manager = C.UIManager()
    self.world.create_entity([self.ui_manager])

    join_code_screen = C.TextInputScreen(lambda join_code: self.game.join_game(join_code), max_length=5, draw_length=6)
    
    main_menu = [
      ("Join Game", lambda _: self.ui_manager.open_screen(join_code_screen)),
      ("Create Game", lambda _: self.game.create_game()),
      ("Play Offline", lambda _: self.game.play_offline()),
      ("Settings", lambda _: self.ui_manager.open_menu(settings_menu))
      #TODO: quit
      #TODO: controls setup
    ]

    settings_menu = [
      ("Server URL", lambda _: self.ui_manager.open_screen(make_server_url_screen(self.game))),
      ("Back", lambda menu: menu.entity.remove()),
    ]

    self.ui_manager.open_menu(main_menu, pos=Vector(32, 32))

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