""" paddle.py
    This is used to create a paddle sprite, which is controlled by the player."""

import pygame, os

class Paddle(pygame.sprite.Sprite):
    """ This class creates a paddle sprite."""
    def __init__(self,disp):
        """ This initializes a paddle sprite.
            disp should be a Surface object on which to place the sprite."""
        pygame.init()
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "paddle.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 550
        self.dx = 30
        self.dy = 30
        self.leftKey = False
        self.rightKey = False

    def update(self):
        """ This updates the paddle sprite.
            It handles the movement of the sprite, based on the player's input."""
        if self.leftKey == True:
            self.rect.centerx -= self.dx
            if self.rect.left < 0:
                self.rect.left = 0
        elif self.rightKey == True:
            self.rect.centerx += self.dx
            if self.rect.right > self.screen.get_width():
                self.rect.right = self.screen.get_width()

    def reset(self):
        """ This resets the paddle sprite.
            It is used to quickly initialize it to several original conditions."""
        self.rect.centerx = 400
        self.rect.centery = 550
        self.leftKey = False
        self.rightKey = False
        self.image = pygame.image.load(os.path.join("images", "paddle.png"))
