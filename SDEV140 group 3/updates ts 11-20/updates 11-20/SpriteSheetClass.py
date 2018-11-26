import pygame, sys, random, time
from pygame.locals import *

class SpriteSheet(object):
    #generic sprite sheet
    #does not currently include anything involving motion of the sprite
    #-that would likely exist as simply changing out the x,y co-ordinantes
    #
    #
    #
    #
    #
    def __init__(self, file_name):
        self.sprite_sheet=pygame.image.load(file_name).convert()
        self.x=-1000
        self.y=-1000
        self.deceleration=0
        self.xSpeed=0
        self.ySpeed=0

        # Helpful variable to assist with collision control TS
        self.hitbox = pygame.Rect(self.x, self.y, 32, 32)

        # Variables to test jump code TS
        self.isJump = False
        self.jumpCount = 15

        # Variable to pass East or West orientation, just cant figure where to 
        # transform image after the slicing of the sprite sheet
        self.orientation = 'E'



    def get_image(self, x, y, width, height):
        #shouldn't need to call this ever, it is called by get_animate and does
        #the function of getting each section of the sprite
        #sheet and returning it as 'image'
        image = pygame.Surface([width,height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x,y,width, height))
        image.set_colorkey((0,0,0))
        return image


    def flip_image(self, image, orientation_x, orientation_y):
        # Function to help change image orientation depending on what direction
        # the sprite is heading in. orientation_x/y accepts True/False.
        flipped_image = pygame.transform.flip(image, orientation_x, orientation_y)
        return flipped_image

    def get_animate(self,frames_to_get,startX,width,height):
        #this function establish what frames are the current cycle of frames
        #presumes the sprites are all the same width and height
        self.frames = []
        x = startX
        y = 0
        for i in range(frames_to_get):
            image = self.get_image(x,y,width,height)
            self.frames.append(image)
            x=x+width
        self.counter= 0

    def motions(self):
        #function to move the sprite in a natural looking manner
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

        self.xSpeed = self.xSpeed - self.deceleration
        self.ySpeed = self.ySpeed - self.deceleration

    def update(self,screen):
        #sort of the bread and butter function
        #calling this advances one of the frames in the frames 'list'
        #need to adjust the sprites self.x and self.y to change its location
        #default self.x self.y are going to be set to -1000 -1000 in the __init__ function
        self.motions()
        self.max = len(self.frames)

        # This code is to update the objects orientation and flip 
        # sprite slice accordingly 
        # Note: this can be done inside the get_image method alternatively (11-20/TS)
        if self.orientation == 'E':
            # Orientation East (11-20/TS)
            print('trip east')
            screen.blit(self.flip_image((self.frames[self.counter]),True,False),(self.x,self.y))
            self.counter=self.counter+1
            if self.counter >= self.max:
                self.counter = 0
        else:
            # Orientation West (11-20/TS)
            print('trip west')
            screen.blit(self.frames[self.counter],(self.x,self.y)) ####
            self.counter=self.counter+1
            if self.counter >= self.max:
                self.counter = 0
