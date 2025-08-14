import pygame
from pygame.locals import *
import random

# DROP CLASS 
class Drop():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dropImage = pygame.image.load("images/drop.png")
        # A rect is made up of [x, y, width, height]
        self.rect = self.dropImage.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.maxWidth = windowWidth - self.width
        
        
        # Pick a random starting position 
        self.x = random.randint(0, self.maxWidth)
        self.y = random.randint(-self.windowHeight, 0) # at or above 0

        # Choose a random speed between 3 and 6 per frame, but not zero
        # in y direction
        self.ySpeed = random.randint(3,6)

    def update(self):
        # drop down by speed
        self.y += self.ySpeed
        # check for hitting the ground, relocate it above the window
        if self.y > self.windowHeight :
            self.x =random.randint(0, self.maxWidth)  #  re-randomize the X position 
            self.y = random.randint(-self.windowHeight, 0)
            self.ySpeed = random.randint(3,6)


    def draw(self):
        self.window.blit(self.dropImage, (self.x, self.y))



