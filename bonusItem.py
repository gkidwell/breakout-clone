""" bonusItem.py
    This is used to create a BonusItem sprite.
    The item is drawn off screen, and the game later places it appropriately.
    """

import pygame, os

class BonusItem(pygame.sprite.Sprite):
    """ """
    def __init__(self,disp,type):
        """ This initializes a BonusItem sprite.
            disp should be a Surface object on which to place the sprite.
            type is an int, and indicates what its image should be.
                0 - pointsbonus.png, a blue gem
                1 - firebonus.png, a red F circle
                2 - stickybonus.png, a green S circle"""
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        if type == 0:
            self.image = pygame.image.load(os.path.join("images", "pointbonus.png"))
        elif type == 1:
            self.image = pygame.image.load(os.path.join("images", "firebonus.png"))
        elif type == 2:
            self.image = pygame.image.load(os.path.join("images", "stickybonus.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 5
        self.rect.centerx = -100
        self.rect.centery = -100
        self.moving = False

    def update(self):
        """ This updates the bonus item sprite.
            This handles the movement of the sprite."""
        if self.moving == True:
            # If it is moving, have it move down on the screen.
            self.rect.centery += self.dy
            if self.rect.top > self.screen.get_height():
                # If it has passed beneath the screen, the player missed it, and it should reset itself.
                self.reset()

    def reset(self):
        """ This resets the bonus item sprite.
            It is used to quickly initialize it to several original conditions."""
        self.rect.centerx = -100
        self.rect.centery = -100
        self.moving = False
