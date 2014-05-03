""" brick.py
    This is used to create a brick sprite."""

import pygame, os

class Brick(pygame.sprite.Sprite):
    """ This class creates a brick sprite."""
    def __init__(self,disp):
        """ This initializes the brick sprite.
            disp should be a Surface object on which to place the sprite."""
        pygame.init()
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        # Load a default image, which will later be changed in-game.
        self.image = pygame.image.load(os.path.join("images", "bluebrick.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = -100

    def changePos(self,x,y):
        """ This changes the position of the brick sprite.
            x should be an int, indicating the intended position for the left side.
            y should be an int, indicating the intended position for the top side.
            These are the amounts of pixels from the left and top of the screen, respectively."""
        self.rect.left = x
        self.rect.top = y

    def update(self):
        """ This would update the brick sprite.
            However, it was determined that nothing needed to be handled here.
            To simplify the the updating of all sprites in the main() method of project4.py (allSprites.update()),
            this was included as an empty method."""

    def reset(self):
        """ This resets the brick sprite.
            It is used to quickly initialize it to several original conditions."""
        self.rect.centerx = -100
        self.rect.centery = -100
