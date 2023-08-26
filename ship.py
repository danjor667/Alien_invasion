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
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            """
            behaving as its in the cosine part of
            the x-y plane. dont know why
            """
        if self.moving_up and self.rect.y > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """
        draw the ship
        """
        self.screen.blit(self.image, self.rect)
