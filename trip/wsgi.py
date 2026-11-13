"""
WSGI config for trip project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import sys
import pygame

def run_game():
    # initializing game and create a screen object.

    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # set the background color
    bg_color = (120, 120, 125)

    # Start the maing loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during 
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

