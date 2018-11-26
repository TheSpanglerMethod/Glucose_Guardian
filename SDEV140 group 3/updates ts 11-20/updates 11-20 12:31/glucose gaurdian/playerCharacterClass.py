import pygame, sys, random, time
from pygame.locals import *
from SpriteSheetClass import *

class PlayerCharacter(SpriteSheet):
    #specfic class for the player character
    def __init__(self, file_name):
        super().__init__(file_name)
        
    def input(self):
        #this function gets what keys are pressed
        #I think something better could replace this
        #
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
        #call function, it calls a pygame function that returns the keys into key variable
        #returns the string of that key for the other function to then read
            

    def movement(self, di, speed):
        #controls the motion of the sprite
        #runs constantly
        #speed should probably be split into which direction of speed
        #currently the deceleration portion really does not do anything
        #
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

##        if self.xSpeed > 0:
##            self.xSpeed = self.xSpeed - self.deceleration
##        if self.ySpeed >0:
##            self.ySpeed = self.ySpeed - self.deceleration
            
        #currently is going to keep reseting speed to 20 every time its called
        #when its called it adjusts the location of the sprite by which keys are pressed
        #setting the x/y co-ordinate to itself and then the change done by the speed variable

    def update(self, screen):
        super().update(screen)
        self.movement(self.input(),20)
        
        
