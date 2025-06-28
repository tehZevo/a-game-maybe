import pygame

import game.components as C
from game.utils import Vector
from game.utils import image_utils
from game.utils.image_cache import get_image
from ..screen import Screen
from game.graphics.character_creator import get_face_images
from game.utils import image_utils

GENDERS = ["male", "female"]
SKIN_TONES = ["pale", "light", "tan", "dark"]
EYE_COLORS = ["blue", "green", "brown", "red"]
NUM_HAIR_STYLES = 2
HAIR_COLORS = ["brown", "green", "blue", "red", "black", "white"]

class CharacterCreationScreen(Screen):
  def __init__(self, lobby_state):
    super().__init__()
    self.lobby_state = lobby_state
    #TODO: meh
    self.ui_manager = None
    self.carousel = 0
    self.gender = "male"
    self.hair_style = 0
    self.skin_tone = "light"
    self.eye_color = "blue"
    self.hair_color = "brown"
    self.carousel_names = ["Gender", "Skin Tone", "Hair Style", "Hair Color", "Eye Color"]
  
  def on_destroy(self):
    self.ui_manager.pop()

  def set_gender(self, selection):
    self.gender = GENDERS[selection]
  
  def set_hair_style(self, selection):
    self.hair_style = selection

  def set_skin_tone(self, selection):
    self.skin_tone = SKIN_TONES[selection]
  
  def set_eye_color(self, selection):
    self.eye_color = EYE_COLORS[selection]
  
  def set_hair_color(self, selection):
    self.hair_color = HAIR_COLORS[selection]

  def start(self):
    self.carousels = [
      C.Carousel(GENDERS, size=8, on_change=self.set_gender),
      C.Carousel(SKIN_TONES, size=8, on_change=self.set_skin_tone),
      C.Carousel([str(i) for i in range(NUM_HAIR_STYLES)], size=8, on_change=self.set_hair_style),
      C.Carousel(HAIR_COLORS, size=8, on_change=self.set_hair_color),
      C.Carousel(EYE_COLORS, size=8, on_change=self.set_eye_color),
    ]

    for i, carousel in enumerate(self.carousels):
      self.entity.world.create_entity([
        C.Position(Vector(16, 64 + 16 * i)),
        carousel
      ])

  def draw(self, renderer):
    for i, name in enumerate(self.carousel_names):
      image_utils.draw_text(renderer, name, Vector(16, 64 - 8 + i * 16), color=(255, 255, 255))

    image_utils.draw_text(renderer, f"Join Code: {self.lobby_state.game.room.join_code}", Vector(0, 0), color=(255, 255, 255))
    self.draw_ready(renderer)
    self.draw_face(renderer)

  def draw_face(self, renderer):
    face_images = get_face_images(self.gender, self.skin_tone, self.hair_style, self.hair_color, self.eye_color)
    for image in face_images:
      renderer.draw(image, Vector(16, 16))

  def handle_keys(self, kbd):
    if kbd.pressed[pygame.K_DOWN]:
      self.carousel += 1
    if kbd.pressed[pygame.K_UP]:
      self.carousel -= 1
    self.carousel = max(0, min(self.carousel, len(self.carousels) - 1))
    
    self.carousels[self.carousel].handle_keys(kbd)

  def draw_ready(self, renderer):
    ready = len(self.lobby_state.ready_players)
    total = len(self.lobby_state.game.room.players)
    image_utils.draw_text(renderer, f"Ready: {ready}/{total}", Vector(0, renderer.height - 8), color=(255, 255, 255))

  def on_destroy(self):
    for carousel in self.carousels:
      carousel.remove()