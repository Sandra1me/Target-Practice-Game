import pygame
import random

# Initialize pygame
pygame.init()

# Create the game window
scr=pygame.display.set_mode((800,600))

pygame.display.set_caption("Target Shooting")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

background=pygame.image.load("background.png")

# Player
playerImg=pygame.image.load("target.png")
playerX, playerY = pygame.mouse.get_pos()

# Enemy
enemyImg=pygame.image.load("dartboard.png")
enemyX=random.randint(64,736)
enemyY=random.randint(64,536)

# Shoot
# shoot_state=ready we cant see it on the screen
# shoot_state=fire we see the shoot
shootImg=pygame.image.load("shoot.png")
shoot_state="ready"
time=0


def player(x,y):
    scr.blit(playerImg,(x,y))

def enemy(x,y):
    scr.blit(enemyImg,(x,y))

def fire(x,y):
    global shoot_state # So we can change the state
    shoot_state="fire"
    scr.blit(shootImg,(x,y))


# Game loop
running=True

while running:  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                fire(playerX,playerY)

    scr.fill((250,250,250))

    #Mouse controls
    pygame.mouse.set_visible(False)
    playerX, playerY = pygame.mouse.get_pos()

    #Create limits for the screen
    if playerX<=0:
        playerX=0
    elif playerX>=750:
        playerX=750

    if playerY<=0:
        playerY=0
    elif playerY>=550:
        playerY=550

    # Background image
    scr.blit(background,(0,0)) # We use blit to add images, and set coordinates

    # Enemy
    enemy(enemyX,enemyY)

    # Shooting
    if time>20:
        shoot_state="redy"
        time=0
    if shoot_state=="fire":
        fire(playerX-6,playerY-6)
        time+=1
        

    # Player
    player(playerX,playerY)


    pygame.display.update()