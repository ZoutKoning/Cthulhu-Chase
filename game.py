import pygame, sys
pygame.init()
import math

#window size Originally set to (800,600)
#background image 1439 pixels wide, 730 pixels high
FrameWidth = 1439
FrameHeight = 730
display = pygame.display.set_mode((FrameWidth, FrameHeight))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

#Bullets
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (0,0,0), (self.x, self.y), 5)

player = Player(400, 300, 32, 32)

display_scroll = [0, 0]

player_bullets = []

#BACKGROUND
# background image size = 1439 pixels wide, 730 pixels high
bg = pygame.image.load("CthulhuChaseBackground.png").convert()
scroll = 0
tiles = math.ceil(FrameWidth / bg.get_width())+1

while True:
    clock.tick(60) #Manages speed of scrolling in pygame
    #display.fill((24,168,86))
    
#------- PLAYER MOVEMENT SECTION -------#

    #Player has/moving Check variables
    playerMovingRight = False
    playerMovingLeft = False
    
    keys = pygame.key.get_pressed()
    pygame.draw.rect(display, (255, 255, 255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))
    
    #Move Left
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        playerMovingLeft = True
        playerMoved = 1
        for bullet in player_bullets:
            bullet.x += 5

    #Move Right    
    if keys[pygame.K_d]:
        display_scroll[0] += 5
        playerMovingRight = True
        playerMoved = 1
        for bullet in player_bullets:
            bullet.x -= 5
    #Move Up        
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.x += 5
    #Move down
    if keys[pygame.K_s]:
        display_scroll[1] += 5
        playerMoving = True

        for bullet in player_bullets:
            bullet.x -= 5
    mouse_x, mouse_y = pygame.mouse.get_pos()


#------- DRAW THINGS TO SCREEN SECTION -------#

#--Background Scrolling--#

    #Scrolls Right to Left
    if(playerMovingRight == True):
        i = 0
        # Append image to the back of same image
        display.blit(bg, (bg.get_width()*i + scroll, 0))
        while(i < tiles):
            display.blit(bg, (bg.get_width()*i + scroll, 0))
            i += 1
            #Frame for scrolling
            scroll -= 3
        #Reset the scroll Frame
        if abs(scroll) > bg.get_width():
            scroll = 0
    
    #Scrolls Left to Right 
    if(playerMovingLeft == True):
        i = 1439
        # Append image to the fromt of same image
        display.blit(bg, (bg.get_width()*i + scroll, 0))
        while(i > tiles):
            display.blit(bg, (bg.get_width()*i - scroll, 0))
            i -=1
            #Frame for scrolling 
            scroll += 2
            #Reset the scroll Frame
        if abs(scroll) < bg.get_width():
            scroll = 0

    #Draw player
    player.main(display)
    #Draw bullets
    for bullet in player_bullets:
        bullet.main(display)
    
    pygame.display.update()


#------- END GAME -------#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

