import pygame

import game.components as C
from game.utils import Vector
from game.utils import image_utils
from game.utils.image_cache import get_image
from ..screen import Screen

FACE_DIR = "assets/player/face/"
gender_eyes = {
  "male": "male_eyes.png",
  "female": "female_eyes.png"
}

gender_hair_styles = {
  "male": ["male_hair_1.png", "male_hair_2.png"],
  "female": ["female_hair_1.png", "female_hair_2.png"],
}

skin_tones = {
  "pale": [242, 210, 179],
  "light": [238, 195, 154],
  "tan": [204, 147, 98],
  "dark": [87, 60, 39],
}

eye_colors = {
  "green": [107, 181, 33],
  "blue": [4, 116, 191],
  "brown": [87, 42, 23],
  "red": [177, 19, 19],
}

hair_colors = {
  "green": [46, 94, 2],
  "blue": [21, 42, 172],
  "brown": [87, 42, 23],
  "red": [177, 19, 19],
  "black": [26, 26, 26],
  "white": [224, 224, 224],
}

#TODO: move to utils?
def get_face_images(gender, skin_tone, hair_style, hair_color, eye_color):
  eyes = get_image(FACE_DIR + gender_eyes[gender])
  
  skin = get_image(FACE_DIR + "skin.png").copy()
  skin.fill(skin_tones[skin_tone], special_flags=pygame.BLEND_MULT)
  
  hair = get_image(FACE_DIR + gender_hair_styles[gender][hair_style]).copy()
  hair.fill(hair_colors[hair_color], special_flags=pygame.BLEND_MULT)
  
  pupils = get_image(FACE_DIR + "pupils.png").copy()
  pupils.fill(eye_colors[eye_color], special_flags=pygame.BLEND_MULT)
  
  return skin, eyes, pupils, hair

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
    self.draw_face(renderer)

  def draw_face(self, renderer):
    face_images = get_face_images("male", "light", 0, "brown", "green")
    for image in face_images:
      renderer.draw(image, Vector(16, 16))

  def draw_ready(self, renderer):
    ready = len(self.lobby_state.ready_players)
    total = len(self.lobby_state.game.room.players)
    image_utils.draw_text(renderer, f"Ready: {ready}/{total}", Vector(0, renderer.height - 8), color=(255, 255, 255))
