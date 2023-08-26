#!/usr/bin/python3
import pygame


class Ship():
    """
    class that manage player's
    ship
    """
    def __init__(self, ai_game):
        """
        doc
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #loading the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #positioning the ship at the bottom centerof the display
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        if self.moving_left:
            if self.rect.left > 0:
                self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """
        draw the ship
        """
        self.screen.blit(self.image, self.rect)
