""" endgame.py
    This is used for the screen at the end of the game."""

import pygame

class EndGame(pygame.sprite.Sprite):
    """ This class displays an appropriate message regarding the outcome of the game,
        and prompts the user to restart if desired."""
    def __init__(self,disp,outcome):
        """ This initializes the End Game screen.
            disp should be a Surface object on which to place the text.
            outcome should be an int
                0 = The Player lost
                1 = The Player won."""
        self.screen = disp
        self.outcome = outcome
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("", 75)

    def update(self):
        """ This updates the End Game Screen.
            Based on the outcome, the appropriate message will show up in the center of the screen."""
        if self.outcome == 0:
            self.text = "YOU LOSE! Press 'R' to restart."
        elif self.outcome == 1:
            self.text = "YOU WIN! Press 'R' to restart."
        self.image = self.font.render(self.text,1, (0, 250, 154))
        self.rect = self.image.get_rect()
        # Display the image in the center of the screen.
        self.rect.centerx = self.screen.get_width() / 2
        self.rect.centery = self.screen.get_height() / 2
