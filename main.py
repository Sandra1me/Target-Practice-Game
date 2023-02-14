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
timeE=0
limit=random.randint(100,200)

# Shoot
# shoot_state=ready we cant see it on the screen
# shoot_state=fire we see the shoot
shootImg=pygame.image.load("shoot.png")
shoot_state="ready"
timeS=0

# Other
score=0
fails=0


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
        
        # Collision
        shootRect=shootImg.get_rect(topleft=(playerX,playerY))
        enemyRect=enemyImg.get_rect(topleft=(enemyX,enemyY))        
        collide=pygame.Rect.colliderect(shootRect,enemyRect)

        if collide and event.type==pygame.MOUSEBUTTONDOWN:
            score+=1
            timeE=0
            enemyX=random.randint(64,736)
            enemyY=random.randint(64,536)


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
    timeE+=1

    if timeE>=limit:
        timeE=0
        fails+=1
        enemyX=random.randint(64,736)
        enemyY=random.randint(64,536)

    # Shooting
    if timeS>20:
        shoot_state="ready"
        timeS=0
    if shoot_state=="fire":
        fire(playerX-6,playerY-6)
        timeS+=1
        

    # Player
    player(playerX,playerY)


    pygame.display.update()