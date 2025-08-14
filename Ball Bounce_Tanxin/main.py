# pygame demo using Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from Drop import * #bring in the Drop class code

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3
N_DROPS = 0

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oInstructions = pygame.image.load('images/instructions.jpg')

# 5 - Initialize variables
ballList = []
dropList = []
for i in range(0, N_BALLS):
    # create a ball object for each ball
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new ball to the list of balls   

for i in range (0, N_DROPS):
    oDrop = Drop(window, WINDOW_WIDTH,WINDOW_HEIGHT)
    dropList.append(oDrop)
    
# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_b:
                oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                ballList.append(oBall)
            elif event.key == K_d:  # each time the user types the letter d, the program should create a new drop
                oDrop = Drop(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                dropList.append(oDrop)

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each ball to update itself
    for oDrop in dropList:
        oDrop.update()  # tell each drop to update itself

   # 9 - Clear the screen before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the screen elements
    window.blit(oInstructions, (85, 430))
    for oBall in ballList:
        oBall.draw()   # tell each ball to draw itself
    for oDrop in dropList:
        oDrop.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


