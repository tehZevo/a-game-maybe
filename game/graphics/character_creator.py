import pygame

from game.utils.image_cache import get_image

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