import pygame
import random

from pygame import mixer

# Initialize pygame
pygame.init()

# Create the game window
scr=pygame.display.set_mode((800,600))

pygame.display.set_caption("Target Shooting")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Background and sound
background=pygame.image.load("background.png")
mixer.music.load("background.mp3")
mixer.music.play(-1)

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

# Score
score_val=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=15

# Fails
fails_val=0

# Game over text
gameover_font=pygame.font.Font("freesansbold.ttf",64)


def player(x,y):
    scr.blit(playerImg,(x,y))

def enemy(x,y):
    scr.blit(enemyImg,(x,y))

def fire(x,y):
    global shoot_state # So we can change the state
    shoot_state="fire"
    scr.blit(shootImg,(x,y))

def show_score(x,y):
    score=font.render("Score: "+ str(score_val), True, (0,0,0))
    scr.blit(score,(x,y))

def show_fails(x,y):
    fails=font.render("Fails: "+ str(fails_val), True, (0,0,0))
    scr.blit(fails,(x,y))

def game_over():
    gameover=gameover_font.render("GAME OVER", True, (0,0,0))
    scr.blit(gameover,(200,250))


# Game loop
running=True

while running:  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                fire(playerX,playerY)
                shoot_sound=mixer.Sound("shoot.mp3")
                shoot_sound.play()
        
        # Collision
        shootRect=shootImg.get_rect(topleft=(playerX,playerY))
        enemyRect=enemyImg.get_rect(topleft=(enemyX,enemyY))        
        collide=pygame.Rect.colliderect(shootRect,enemyRect)

        if collide and event.type==pygame.MOUSEBUTTONDOWN:
            score_val+=1
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
        fails_val+=1
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

    # Score
    show_score(textX,textY)
    show_fails(textX,textY+47)

    if fails_val>=5:
        game_over()
        fails_val=5
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                break

    pygame.display.update()