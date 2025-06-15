from game.graphics import Spritedef, Animation, Layer

walk_down_body = Layer("assets/player/walk_down_body.png", 16, 4)
walk_down_eyes = Layer("assets/player/walk_down_eyes.png", 16, 4)
walk_down_hair = Layer("assets/player/walk_down_hair.png", 16, 4)

walk_down = Animation(
  layers=[walk_down_body, walk_down_eyes, walk_down_hair],
  loop=True
)

idle_down_body = Layer("assets/player/idle_down_body.png", 16, 1)
idle_down_eyes = Layer("assets/player/idle_down_eyes.png", 16, 1)
idle_down_hair = Layer("assets/player/idle_down_hair.png", 16, 1)

idle = Animation(
  layers=[idle_down_body, idle_down_eyes, idle_down_hair],
  loop=False
)

player = Spritedef(
  id="player",
  animations = {
    "walk_down": walk_down,
    "idle": idle
  }
)