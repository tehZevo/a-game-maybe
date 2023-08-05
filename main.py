import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((75, 25))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

player = Player()

x = 0
y = 0

pygame.display.set_caption("Hello World")
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x -= 1
      if event.key == pygame.K_RIGHT:
        x += 1

  # Fill the screen with black
  screen.fill((0, 0, 0))

  # Draw the player on the screen
  screen.blit(player.surf, (x, y))
  clock.tick(60) #limit fps TODO: remove

  # Update the display
  pygame.display.flip()
