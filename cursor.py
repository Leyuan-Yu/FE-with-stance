import pygame
from pygame.locals import *

ANIMATION_FRAME = 6
MOVE_FRAME = 6

image_set = [
    pygame.image.load("Assets/img/Misc/Cursor/sprite_0.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_1.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_2.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_3.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_0.png"),
]


class cursor (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        #positional
        self.x_pos = x
        self.y_pos = y
        self.rect = (self.x_pos*32,self.y_pos*32)
        self.move_frame = 0
        self.can_move = True
        
        #animation
        self.image_set = image_set
        self.index = 0
        self.indexMax = len(self.image_set)
        self.current_frame = 0
        self.image = self.image_set[self.index]

    def move_cursor(self, boundary:list):
        pressed_keys  = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.can_move:
            if self.x_pos > 0:
                self.move_left()
                self.can_move = False
            else:
                self.x_pos = 0
                self.update_rect()
        if pressed_keys[K_RIGHT] and self.can_move:
            if self.x_pos < boundary[0]-1:
                self.move_right()
                self.can_move = False
            else:
                self.x_pos = boundary[0]-1
                self.update_rect()
        if pressed_keys[K_UP] and self.can_move:
            if self.y_pos > 0:
                self.move_up()
                self.can_move = False
            else:
                self.y_pos = 0
                self.update_rect()
        if pressed_keys[K_DOWN] and self.can_move:
            if self.y_pos < boundary[1]-1:
                self.move_down()
                self.can_move = False
            else:
                self.y_pos = boundary[1]-1
                self.update_rect()
    
    def move_left(self):
        self.x_pos -=1
        self.update_rect()

    def move_right(self):
        self.x_pos +=1
        self.update_rect()

    def move_up(self):
        self.y_pos -=1
        self.update_rect()

    def move_down(self):
        self.y_pos +=1
        self.update_rect()
        
    def update_rect(self):
        self.rect = (self.x_pos*32,self.y_pos*32)

    def cursor_pos(self)->tuple[int,int]:
        return (self.x_pos,self.y_pos)

    def update_sprite(self):
        if self.move_frame < MOVE_FRAME:
            self.move_frame += 1
        else:
            self.move_frame = 0
            self.can_move = True
        #tick current frame by 1 if not yet for animation
        if self.current_frame < ANIMATION_FRAME:
            self.current_frame += 1
        #if current frame = animation frame
        else:
            if self.index < self.indexMax-1:
                self.index +=1
            else:
                self.index = 0
            self.update_image()
            self.current_frame = 0

    def update_image(self):
        self.image = self.image_set[self.index]

self = cursor()