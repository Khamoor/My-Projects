import pygame
import sys

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    pygame.display.set_mode((500, 500))
    pygame.display.set_caption("keys")
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()