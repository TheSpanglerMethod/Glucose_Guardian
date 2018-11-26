import pygame, sys, random, time
from pygame.locals import *

class SpriteSheet(object):
    #generic sprite sheet
    def __init__(self, file_name):
        self.sprite_sheet=pygame.image.load(file_name).convert()
        self.x=-1000
        self.y=-1000
        self.deceleration=1
        self.xSpeed=0
        self.ySpeed=0

#==============================================================================#
#==============================================================================#
    def get_image(self, x,y, width, height):
        #shouldn't need to call this ever, it is called by get_animate and does the function of getting each section of the sprite
        #sheet and returning it as 'image'
        image = pygame.Surface([width,height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x,y,width, height))
        image.set_colorkey((255,255,255))
        return image

    def get_reverse_image(self, x,y, width,height):
        image = pygame.Surface([width,height]).convert()
        image.blit(pygame.transform.flip(self.sprite_sheet, False, True), (0,0), (x,y,width, height))
        image.set_colorkey((255,255,255))
        return image
    
    def motions(self):
        #function to move the sprite in a natural looking manner
        #currently does not work
        #known issues:
        #1.Does not move in a natural manner
        #2.Since it clears the speed passed 0 it cannot go negativly
        #IE up or to the left
        
        
        if self.xSpeed >= 0:
            self.x=self.x+self.xSpeed
            self.xSpeed=self.xSpeed-self.deceleration
        elif self.ySpeed >= 0:
            self.y=self.y+self.ySpeed
            self.ySpeed=self.ySpeed-self.deceleration

#==============================================================================#
#==============================================================================#
               
    def get_image_v2(self, x,y, width,height, VerticalFlip,HorizontalFlip,):
        image = pygame.Surface([width,height]).convert()
        image.blit(pygame.transform.flip(self.sprite_sheet, VerticalFlip, HorizontalFlip), (0,0), (x,y,width, height))
        image.set_colorkey((255,255,255))#whatever color this is set to is removed from the image displayed
        return image
    
    def get_animate(self,frames_to_get,startX,width,height):
        #this function establish what frames are the current cycle of frames
        #presumes the sprites are all the same width and height
        self.frames = []
        x = startX
        y = 0
        for i in range(frames_to_get):
            image = self.get_reverse_image(x,y,width,height)
            self.frames.append(image)
            x=x+width
        self.counter= 0

    def update(self,screen):
        #sort of the bread and butter function
        #calling this advances one of the frames in the frames 'list'
        #need to adjust the sprites self.x and self.y to change its location
        #default self.x self.y are going to be set to -1000 -1000 in the __init__ function

        self.max = len(self.frames)
        screen.blit(self.frames[self.counter],(self.x,self.y))
        self.counter=self.counter+1
        if self.counter >= self.max:
            self.counter = 0
