import pygame, sys, random, time
from pygame.locals import *
from SpriteSheetClass import *

class PlayerCharacter(SpriteSheet):
    def move(self,di, speed):
        self.directions={
        1:"up",
        2:"left",
        3:"down",
        4:"right"
        }
        if self.directions[di]=="up":
            self.ySpeed=100
        elif self.directions[di]=="down":
            self.ySpeed=-100
        elif self.directions[di]=="right":
            self.xSpeed=100
        elif self.directions[di]=="left":
            self.xSpeed=-100
        
