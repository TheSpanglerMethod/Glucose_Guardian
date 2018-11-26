import pygame, sys, random, time
from pygame.locals import *
from SpriteSheetClass import *

class PlayerCharacter(SpriteSheet):
    #specfic class for the player character
    def __init__(self, file_name):
        super().__init__(file_name)
        self.facing = "LEFT"
        self.wentW = 0
        self.wentE = 0
        self.currentKeys = []
        
        #TS-Jump
        self.isJump= False
        self.jumpCount = 15
        
    def input(self):
        #this function gets what keys are pressed
        #I think something better could replace this
        #
        self.currentKeys=[]
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.currentKeys.append("DOWN")
        if key[pygame.K_UP]:
            self.currentKeys.append("UP")
        if key[pygame.K_RIGHT]:
            self.currentKeys.append("RIGHT")
        if key[pygame.K_LEFT]:
            self.currentKeys.append("LEFT")
        if key[pygame.K_SPACE]: #TS-Jump
            self.currentKeys.append("JUMP")
        #call function, it calls a pygame function that returns the keys into key variable
        #returns the string of that key for the other function to then read
        return self.currentKeys
            

    def movement(self, di, speed):
        #controls the motion of the sprite
        #runs constantly
        #speed should probably be split into which direction of speed
        #currently the deceleration portion really does not do anything
        #
        self.ySpeed =speed
        self.xSpeed =speed
        if "UP" in di:
            self.y=self.y-self.ySpeed
        if "DOWN" in di:
            self.y=self.y+self.ySpeed
        if "RIGHT" in di:
            self.x=self.x+self.xSpeed
            if self.facing=="LEFT":
                self.facing="RIGHT"
                self.get_animate(6,0,0,32,32,True, False)
        if "LEFT" in di:
            self.x=self.x-self.xSpeed
            if self.facing=="RIGHT":
                self.facing="LEFT"
                self.get_animate(6,0,0,32,32,False, False)
        if "JUMP" in di: #TS-Jump
            if self.jumpCount >= 15:
                neg = 1
                if self.jumpCount <0:
                    neg = -1
                self.y -= (self.jumpCount **2) *.125 * neg
            else:
                self.isJump = False
                self.jumpCount -=5
            
        #currently is going to keep reseting speed to 20 every time its called
        #when its called it adjusts the location of the sprite by which keys are pressed
        #setting the x/y co-ordinate to itself and then the change done by the speed variable

    def update(self, screen):
        super().update(screen)
        self.movement(self.input(),20)
        
        
