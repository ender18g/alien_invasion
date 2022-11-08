import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.1)
        self.rect = self.image.get_rect()

        # start alien at top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move alien right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

