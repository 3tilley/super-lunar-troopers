import pygame
from pygame.locals import *

import random

if not pygame.font:
    raise RuntimeError("Install pygame.font")

def boukie_function(x, y):
    """Fill a circle at a point x,y"""
    # Boukie fill this in


def main():
    pygame.init()
    width = 400
    height = 400
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Super Lunar Troopers")
    # pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    font = pygame.font.Font(None, 36)
    text = font.render("Click for a new colour", 1, (10,10,10))
    textpos = text.get_rect(centerx=background.get_width() / 2)

    clock = pygame.time.Clock()

    going = True
    while going:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == MOUSEBUTTONUP:

                colours = [random.randint(0,250) for i in range(3)]
                background.fill(tuple(colours))

            elif event.type == KEYUP:
                w = random.randint(0, width)
                h = random.randint(0, height)
                boukie_function(w, h)

            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()

if __name__ == "__main__":
    main()
