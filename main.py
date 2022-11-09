import pygame

# Initialize pygame
pygame.init()

# Create the game window
scr=pygame.display.set_mode((800,600))

pygame.display.set_caption("Target Shooting")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg=pygame.image.load("target.png")
playerX, playerY = pygame.mouse.get_pos()


def player(x,y):
    scr.blit(playerImg,(x,y))


# Game loop
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

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

    player(playerX,playerY)



    pygame.display.update()