import pygame, sys, random, time
from pygame.locals import *
from SpriteSheetClass import *

class PlayerCharacter(SpriteSheet):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.directions={
        "up":1,
        "left":2,
        "down":3,
        "right":4
        }

#==============================================================================#
#==============================================================================#
    def get_inputs(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            return 1
        elif key[pygame.K_UP]:
            return 3
        elif key[pygame.K_RIGHT]:
            return 4
        elif key[pygame.K_LEFT]:
            return 2
        elif key[pygame.K_SPACE]:
            self.x=100
            self.y=100
            return 0
    
    def move(self,di, speed):
        if di==1:
            self.ySpeed=10
        elif di==3:
            self.ySpeed=-10
        elif di==4:
            self.xSpeed=10
        elif di==2:
            self.xSpeed=-10
#==============================================================================#
#==============================================================================#            
    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            return "DOWN"
        elif key[pygame.K_UP]:
            return "UP"
        elif key[pygame.K_RIGHT]:
            return "RIGHT"
        elif key[pygame.K_LEFT]:
            return "LEFT"
        elif key[pygame.K_SPACE]:
            self.x=100
            self.y=100
            return "NULL"
            

    def movement(self, di, speed):
        self.ySpeed =speed
        self.xSpeed =speed
        if di == "UP":
            self.y=self.y-self.ySpeed
        elif di == "DOWN":
            self.y=self.y+self.ySpeed
        elif di == "RIGHT":
            self.x=self.x+self.xSpeed
        elif di == "LEFT":
            self.x=self.x-self.xSpeed

        if self.xSpeed > 0:
            self.xSpeed = self.xSpeed - self.deceleration
        if self.ySpeed >0:
            self.ySpeed = self.ySpeed - self.deceleration

    def update(self, screen):
        super().update(screen)
        #self.move(self.get_inputs(),20)
        self.movement(self.input(),20)
        
        
