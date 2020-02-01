import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship, a group of bullets and a group of aliens.
    ship = Ship(screen)
    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()