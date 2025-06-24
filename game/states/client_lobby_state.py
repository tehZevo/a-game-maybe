from game.ecs import World
import game.components as C
import game.networking.commands as commands
import game.networking.events as E
import game.networking.commands as commands
from game.utils import Vector

class ClientLobbyState:
  def __init__(self, game, channel, join_code):
    self.game = game
    self.channel = channel
    self.join_code = join_code
    self.channel.setup_handlers([
      #TODO
    ])

    self.world = World()
    self.world.create_entity([
      C.Position(Vector(32, 32)),
      C.TextField(lambda text: print(text), draw_length=6, max_length=5)
    ])

    self.renderer = self.world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])
    
    print("[Client] Hello lobby state")

    #TODO: send hello lobby and await lobbystateupdated
    # print("[Client] Join code is", join_code, "but we don't care, starting game...")
    # self.channel.send(commands.PlayerReady())
    
  def step(self, pressed, held, released, pressed_unicode):
    self.channel.handle_events()

    #control player (and other keyhandlers like menus)
    for key_handler in self.world.find_components(C.KeyHandler):
      key_handler.handle_keys(pressed, held, released, pressed_unicode)

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)
