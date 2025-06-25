import game.components as C

from game.utils import Vector
from .screen import Screen

from game.utils import image_utils

class LobbyScreen(Screen):
  def __init__(self, lobby_state):
    super().__init__()
    self.lobby_state = lobby_state
    #TODO: meh
    self.ui_manager = None
  
  def on_destroy(self):
    self.ui_manager.pop()

  #TODO: draw players + usernames
  #TODO: draw player ready states per player
  def draw(self, renderer):
    image_utils.draw_text(renderer, f"Join Code: {self.lobby_state.game.room.join_code}", Vector(0, 0), color=(255, 255, 255))
    self.draw_ready(renderer)

  def draw_ready(self, renderer):
    ready = len(self.lobby_state.ready_players)
    total = len(self.lobby_state.game.room.players)
    image_utils.draw_text(renderer, f"Ready: {ready}/{total}", Vector(0, renderer.height - 8), color=(255, 255, 255))
