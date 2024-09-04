import pygame
from pygame.locals import *

image_set = [
    pygame.image.load("Assets/img/Misc/Cursor/sprite_0.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_1.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_2.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_3.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_4.png"),
]



class cursor (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        self.x_pos = x
        self.y_pos = y
        self.rect = (self.x_pos*32,self.y_pos*32)
        
        self.index = 0
        self.current_frame = 0
        self.image_set = image_set
        self.image = self.image_set[self.index]
    
    def move_left(self):
        self.x_pos -=1
        self.rect = (self.x_pos*32,self.y_pos*32)

    def move_right(self):
        self.x_pos +=1
        self.rect = (self.x_pos*32,self.y_pos*32)

    def move_up(self):
        self.y_pos -=1
        self.rect = (self.x_pos*32,self.y_pos*32)

    def move_down(self):
        self.y_pos +=1
        self.rect = (self.x_pos*32,self.y_pos*32)


new_cursor = cursor()