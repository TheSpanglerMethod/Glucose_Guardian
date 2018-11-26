import pygame, sys, random, time
from pygame.locals import *
from SpriteSheetClass import *

class PlayerCharacter(SpriteSheet):
    def move(self,di,speed):
        self.directions={
        1:"up",
        2:"left",
        3:"down",
        4:"right"
        }
        # This is redundant jump code, not properly functional yet. 
        # Space bar provides functional jump, just attempting to 
        # migrate to up arrow key
        if self.directions[di]=="up":
            if self.jumpCount >= 15:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount **2) *.125 * neg
                self.jumpCount -= 5
            else:
                self.isJump = False
                self.jumpCount = 15
        elif self.directions[di]=="down":
            self.ySpeed=5
        elif self.directions[di]=="right":
            self.xSpeed=5
            self.orientation = 'E'
        elif self.directions[di]=="left":
            self.xSpeed=-5
            self.orientation = 'W'
        
# Is the dictionary necessary? Seems like it woud be easier to 
# pass the string directly through instead of translating (11-20/TS)

