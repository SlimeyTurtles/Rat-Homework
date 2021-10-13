import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])

# Runs until user asks to quit
running = True
while running:

    # Did the user click window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Fill background with white
screen.fill((255, 255, 255))

#Create a surface pass length adn width
surf = pygame.Surface ((50,50))

#Give floor different background
surf.fill((0, 0, 0))
rect = surf.get_rect()

#CONTROLS
from pygame.locals import (
    W_UP,
    S_DOWN,
    A_LEFT
D_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,
)


#Screen size
SCREEN_WIDTH = 800
SCREEN HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        #Did the user press a key
        if event.type == KEYDOWN:
            #Was this key esc
            if event.key == K_ESCAPE:
                running = False

            elif event.type == QUIT:
                running = False
#h





#Done
pygame.quit()

