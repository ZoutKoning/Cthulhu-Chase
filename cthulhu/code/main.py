import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
showtime = False
if(showtime == False):
    screen = pygame.display.set_mode((menuWidth, menuHeight))  
clock = pygame.time.Clock()
level = Level(level_map1,screen)
CURRENT_LEVEL = 1
transparent = (0,0,0)
StartMenu = pygame.image.load("startmenu.jpg")
winner = pygame.image.load("BigWinner.jpg")
bg = pygame.image.load("background.jpg")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Start Menu
    if(showtime == False):
        if(CURRENT_LEVEL < 4):
            screen.blit(StartMenu, (0, 0))
            color = (0,0,0)
        else:
            screen.blit(winner, (0, 0))
            color = (0,0,0)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuWidth/4 <= mouse[0] <= menuWidth/4 + 320 and menuHeight/3 <= mouse[1] <= menuHeight/3 + 60 and CURRENT_LEVEL < 4:
                screen.fill(transparent)
                showtime = True
                screen = pygame.display.set_mode((screen_width,screen_height))
                
            elif menuWidth/4 <= mouse[0] <= menuWidth/4 + 320 and menuHeight/2+10 <= mouse[1] <= menuHeight/2+10 + 60:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        mouse = pygame.mouse.get_pos()
            


    if(showtime == True):
        screen.blit(bg, (0, 0))
        if(CURRENT_LEVEL < 4):
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
            if(level.horizontal_goalpost_collision()):
                level = Level(level_map4, screen)
                showtime = False
                screen = pygame.display.set_mode((menuWidth,menuHeight))
                CURRENT_LEVEL+=1
                                        
    pygame.display.update()
    clock.tick(60)