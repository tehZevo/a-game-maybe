from game.graphics import SimpleSprite

def make_slime(color):
  return SimpleSprite(f"{color}_slime", f"assets/monsters/{color}_slime_idle.png", 16, 4, loop=True)

slime = SimpleSprite("slime", "assets/monsters/slime_idle.png", 16, 4, loop=True)
green_slime = make_slime("green")
purple_slime = make_slime("purple")
gold_slime = make_slime("gold")
dark_slime = make_slime("dark")
pink_slime = make_slime("pink")
brown_slime = make_slime("brown")
red_slime = make_slime("red")