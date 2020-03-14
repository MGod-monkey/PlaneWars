import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
ck = (127, 33, 33)
size = 25
while True:
  if pygame.event.get(pygame.MOUSEBUTTONDOWN):
    s = pygame.Surface((50, 50))

    # first, "erase" the surface by filling it with a color and
    # setting this color as colorkey, so the surface is empty
    s.fill(ck)
    s.set_colorkey(ck)

    pygame.draw.circle(s, (255, 0, 0), (size, size), size, 2)

    # after drawing the circle, we can set the
    # alpha value (transparency) of the surface
    s.set_alpha(75)

    x, y = pygame.mouse.get_pos()
    screen.blit(s, (x-size, y-size))

  pygame.event.poll()
  pygame.display.flip()