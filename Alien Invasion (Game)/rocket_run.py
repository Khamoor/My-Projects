import pygame
from settings import Settings
from rocket import Rocket
import check_events as ce


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
            (r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship, a group of bullets and a group of aliens.
    rocket = Rocket(r_settings, screen)
    
    # Start the main loop for the game.
    while True:
        ce.check_events(r_settings, screen, rocket)
        rocket.update()
        ce.update_screen(r_settings, screen, rocket)
        
run_game()