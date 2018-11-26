import pygame, sys, random, time
from pygame.locals import *

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet=pygame.image.load(file_name).convert()

    def get_image(self, x,y, width, height):
        image = pygame.Surface([width,height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x,y,width, height))
        image.set_colorkey((0,0,0))
        return image
    
    def get_animate(self,frames_to_get,startX,width,height):
        #this function makes the 'animation'
        self.frames = []
        x = startX
        y = 0
        print("animating")
        for i in range(frames_to_get):
            print(i, "frame")
            image = self.get_image(x,y,width,height)
            self.frames.append(image)
            x=x+width
        print(self.frames)
        self.counter= 0
            
    def animate(self):#this function does not work
        for x in self.frames:
            screen.blit(x,(200,200))
            pygame.display.update()

    def update(self):   #calling this each iteration makes them advance one frame
                        #in the created animation
        self.max = len(self.frames)
        screen.blit(self.frames[self.counter],(200,200))
        self.counter=self.counter+1
        if self.counter >= self.max:
            self.counter = 0
            

pygame.init()
height = 1000
width  = 1000
size = height,width
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)
ss = SpriteSheet("Slime_spacee.png")
ss.get_image(0,0,32,32)
ss.get_animate(6,0,32,32)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    objects_to_update.update()




    #should probs be last always
    #submits all prior changes to the screen
    #time.sleep(.05)
    clock.tick(5)
    pygame.display.update()
