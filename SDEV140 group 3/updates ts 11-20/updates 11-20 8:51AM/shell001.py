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
bg = pygame.image.load('bg.png') # This loads a background image set to var "bg" TS
pygame.display.set_caption("Glucouse Guardian")

ss = PlayerCharacter("Slime_Space.png")
ss.get_animate(6,0,32,32)
ss.x=100
ss.y=100

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(color["black"])
	# screen.blit(bg,(0,0)) # Paints new background over the black fill TS



	# This is basic code for retrieving keys being held down
	key = pygame.key.get_pressed()

	####### Functional Movement ############### (11-20/TS)
	# 'and' statements keep sprite within confines of screen
	# if key[pygame.K_LEFT] and ss.x > 0:
	# 	ss.x -= 4
	# 	ss.orientation = 'W'
	# if key[pygame.K_RIGHT] and ss.x < 664:
	# 	ss.x += 4
	# 	ss.orientation = 'E'

	# New code testing existing movement options within Player Character Class (11-20/TS)
	if key[pygame.K_UP]:
		ss.move(1,0)
	if key[pygame.K_LEFT]:
		ss.move(2,0)
	if key[pygame.K_RIGHT]:
		ss.move(4,0)



	# I think this should be moved to the player character class sheet,
	# just need to figure out how as it was glitching when I tried last (11-20/TS)

	# Part of jump code ensuring jump is not already engaged before executing jump TS
	if not(ss.isJump):
		if key[pygame.K_SPACE]:
			ss.isJump = True
	# A bit of code taken from a tutorial and *partially* adapted to this games
	# variables that create a "normal" looking parabolic "jump"
	else:
		if ss.jumpCount >= -15:
			neg = 1
			if ss.jumpCount < 0:
				neg = -1
			ss.y -= (ss.jumpCount **2) * .125 * neg
			ss.jumpCount -= 5
		else:
			ss.isJump = False
			ss.jumpCount = 15
	#########################################


	ss.update(screen)
	clock.tick(10)
	pygame.display.update()
