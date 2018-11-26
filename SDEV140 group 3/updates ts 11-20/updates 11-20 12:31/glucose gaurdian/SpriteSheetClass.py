import pygame, sys, random, time
from pygame.locals import *

class SpriteSheet(object):
    #generic sprite sheet
    #Handles Initializing a Sprite and how to grab animation frames for that sprite
    #Movment of each sprite should be handled by its individual sub-class
    #
    def __init__(self, file_name):
        self.sprite_sheet=pygame.image.load(file_name).convert()
        self.x=-1000
        self.y=-1000
        self.deceleration=1
        self.xSpeed=0
        self.ySpeed=0

               
    def get_image_v2(self, x,y, width,height, VerticalFlip,HorizontalFlip,):
        #This function Grabs the image space you provide co-ordinates for
        #VerticalFlip and HorizontalFlip are Boolean Variables, False if you don't want that flip True if you do want that flip
        #
        image = pygame.Surface([width,height]).convert()
        image.blit(pygame.transform.flip(self.sprite_sheet, VerticalFlip, HorizontalFlip), (0,0), (x,y,width, height))
        image.set_colorkey((255,255,255))#whatever color this is set to is removed from the image displayed
        return image
        #the image variable is essentially an unseen screen
        #in pygame its a called a surface
        #calling this function writes onto the image 'screen' what section of that sprite you passed to it earlier
        #then it ejects out what is on that screen as the variable image
    
    def get_animate(self,frames_to_get,startX,startY,width,height,VerticalFlip, HorizontalFlip):
        #this function establish what frames are the current cycle of frames
        #presumes the sprites are all the same width and height
        #adjusting the y changes what row its at
        #adjusting the x changes what column its at
        self.frames = []
        x = startX
        y = startY
        for i in range(frames_to_get):
            image = self.get_image_v2(x,y,width,height,VerticalFlip, HorizontalFlip)
            self.frames.append(image)
            x=x+width
        self.counter= 0
        #the loop runs for how many frames_to_get
        #each pass uses the get_image_v2 function and returns an image
        #the image is then added to a list of images

    def update(self,screen):
        #sort of the bread and butter function
        #calling this advances one of the frames in the frames 'list'
        #need to adjust the sprites self.x and self.y to change its location
        #default self.x self.y are going to be set to -1000 -1000 in the __init__ function
        #
        self.max = len(self.frames)
        screen.blit(self.frames[self.counter],(self.x,self.y))
        self.counter=self.counter+1
        if self.counter >= self.max:
            self.counter = 0

        #each time this is called its going to advance one 'image/frame' in the list of 'images/frames' made by the get_animate function
        #as well as put itself on whatever x/y co-ordinate its current x and y equal
