import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map1,screen)
CURRENT_LEVEL = 1

bg = pygame.image.load("background.jpg")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.blit(bg, (0, 0))
	#screen.fill('black')
	level.run()

	if(CURRENT_LEVEL == 1):
		if(level.horizontal_enemy_collision()):
			level = Level(level_map1,screen)
		if(level.horizontal_goalpost_collision()):
			level = Level(level_map2, screen)
			CURRENT_LEVEL+=1
	elif(CURRENT_LEVEL == 2):
		if(level.horizontal_enemy_collision()):
			level = Level(level_map2,screen)
		if(level.horizontal_goalpost_collision()):
			level = Level(level_map3, screen)
			CURRENT_LEVEL+=1
	elif(CURRENT_LEVEL == 3):
		if(level.horizontal_enemy_collision()):
			level = Level(level_map3,screen)

	pygame.display.update()
	clock.tick(60)