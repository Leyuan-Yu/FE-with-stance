import pygame
from pygame.locals import *
import func

ANIMATION_FRAME = 6
MOVE_FRAME = 6

image_set = [
    pygame.image.load("Assets/img/Misc/Cursor/sprite_0.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_1.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_2.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_3.png"),
    pygame.image.load("Assets/img/Misc/Cursor/sprite_0.png"),
]

func.bind_key()


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

    def cursor_action(self, boundary:list) -> str:
    # get key pressed and handle input
        pressed_keys  = pygame.key.get_pressed()
        if pressed_keys[func.yes_key]:
            return('yes')
        if pressed_keys[func.left_key] and self.can_move:
            return(self.left_key_pressed())
        if pressed_keys[func.right_key] and self.can_move:
            return(self.right_key_pressed(boundary[0]))
        if pressed_keys[func.up_key] and self.can_move:
            return(self.up_key_pressed())
        if pressed_keys[func.down_key] and self.can_move:
            return(self.down_key_pressed(boundary[1]))

    def left_key_pressed(self) ->str:
        if self.x_pos > 0:
            self.move_left()
            self.can_move = False
            return ('left')
        else:
            self.x_pos = 0
            self.update_rect()
            self.can_move = False
            return ('left_scroll')
        
    def right_key_pressed(self,x_boundary) -> str:
        if self.x_pos < x_boundary-1:
            self.move_right()
            self.can_move = False
            return ('right')
        else:
            self.x_pos = x_boundary-1
            self.update_rect()
            self.can_move = False
            return ('right_scroll')
        
    def up_key_pressed(self) -> str:
        if self.y_pos > 0:
            self.move_up()
            self.can_move = False
            return ('up')
        else:
            self.y_pos = 0
            self.update_rect()
            self.can_move = False
            return ('up_scroll')
        
    def down_key_pressed(self, y_boundary) -> str:
            if self.y_pos < y_boundary-1:
                self.move_down()
                self.can_move = False
                return ('down')
            else:
                self.y_pos = y_boundary-1
                self.update_rect()
                self.can_move = False
                return ('down_scroll')
        
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

    def set_cursor_pos(self,cursor_pos:list[int,int]):
        self.x_pos = cursor_pos[0]
        self.y_pos = cursor_pos[1]
        print(self.x_pos,self.y_pos)
        self.update_rect()        

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



if __name__ == "__main__":
    print(func.up_key)