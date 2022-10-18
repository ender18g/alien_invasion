import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        # Ship icon from good ware
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale_by(self.image, (0.5,0.5))


        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)