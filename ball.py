""" ball.py
    This is used to create a ball sprite, which will bounce around the screen."""

import pygame, os

class Ball(pygame.sprite.Sprite):
    """ This class creates a ball sprite."""
    def __init__(self,disp):
        """ This initializes a ball sprite.
            disp should be a Surface object on which to place the sprite."""
        pygame.init()
        pygame.mixer.init()
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "ball.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 530
        self.dx = 10
        self.dy = 10
        self.moving = False
        # These directions are used as simple indicators for the ball's orientation.
        self.down = self.left = 0
        self.up = self.right = 1
        self.ydirection = self.up
        self.xdirection = self.right
        # self.lost used for when ball is off screen.
        self.lost = False
        # self.fire is used for the Fire bonus.
        self.fire = False
        # self.sticky is used for the Sticky bonus.
        self.sticky = False
        self.wallbounce = pygame.mixer.Sound(os.path.join("sounds", "wallbounce.ogg"))

    def update(self):
        """ This updates the ball sprite.
            This handles the movement of the ball, and bouncing off the left, right, and top sides of the screen.
            If it goes beyond the bottom, it is lost."""
        if self.moving == True:
            # If the ball is moving, depending on its ydirection and xdirection values,
            # have it move in the appropriate direction.
            if self.ydirection == self.up:
                self.rect.centery -= self.dy
                if self.rect.top < 0:
                    # If the ball hits the top of the screen, reverse y direction.
                    self.rect.top = 0
                    self.ydirection = self.down
                    self.wallbounce.play()
            elif self.ydirection == self.down:
                self.rect.centery += self.dy
                if self.rect.top > self.screen.get_height():
                    # If the ball has gone off the bottom of the screen, the player lost it.
                    self.lost = True
            if self.xdirection == self.right:
                self.rect.centerx += self.dx
                if self.rect.right > self.screen.get_width():
                    # If the ball hits the right side of the screen, reverse x direction.
                    self.rect.right = self.screen.get_width()
                    self.xdirection = self.left
                    self.wallbounce.play()
            elif self.xdirection == self.left:
                self.rect.centerx -= self.dx
                if self.rect.left < 0:
                    # If the ball hits the left side of the screen, reverse x direction.
                    self.rect.left = 0
                    self.xdirection = self.right
                    self.wallbounce.play()

    def reset(self):
        """ This resets the ball sprite.
            It is used to quickly initialize it to several original conditions."""
        self.moving = False
        self.dx = 10
        self.dy = 10
        self.ydirection = self.up
        self.xdirection = self.right
        self.rect.centerx = 400
        self.rect.centery = 530
        self.fire = False
        self.sticky = False
        self.image = pygame.image.load(os.path.join("images", "ball.png"))
