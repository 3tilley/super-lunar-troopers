import pygame
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Luna shall be free')
screen.fill(background_colour)
pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False