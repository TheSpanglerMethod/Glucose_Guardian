import pygame, sys, random
from pygame.locals import *
from playerCharacterClass import *
from colorsDict import *
pygame.init()
height = 700
width  = 700
size = height,width
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Glucouse Guardian")

ss = PlayerCharacter("Slime_Full_Sheet.png")
ss.get_animate(6,0,57,32,32,False,False)
ss.x=100
ss.y=100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  
            pygame.quit()
            sys.exit()
    screen.fill(color["blue"])
    ss.update(screen)
    clock.tick(30)
    pygame.display.update()
