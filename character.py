import sys
import pygame
from pygame.locals import *

dict = {
    'test': pygame.image.load('Assets/img/Character/C_test.png'),
    'test_selected': pygame.image.load('Assets/img/Character/c_test_select.png'),
    'test_moved' : pygame.image.load('Assets/img/Character/c_test_moved.png'),
}

class character(pygame.sprite.Sprite):
    def __init__(self,character_id:str,char_pos:list[int,int],map_offset:list[int,int]):
        super().__init__()
        self.id =  character_id

        #character and sprite position
        self.char_x_pos = char_pos[0]
        self.char_y_pos = char_pos[1]
        self.map_x_offset = map_offset[0]
        self.map_y_offset = map_offset[1]
        self.char_x_onscreen = self.char_x_pos-self.map_x_offset
        self.char_y_onscreen = self.char_y_pos-self.map_y_offset
        self.rect = (self.char_x_onscreen*32,self.char_y_onscreen*32)

        #image
        self.image = dict['test']

        #movement
        self.selected = False
        self.moved = False
    
    def pos_onscreen(self) -> tuple[int,int]:
        return (self.char_x_onscreen,self.char_y_onscreen)
    
    def char_pos(self) -> tuple[int,int]:
        return (self.char_x_pos,self.char_y_pos)
    
    def char_selected(self):
        self.selected = True
        self.image = dict['test_selected']

    def char_unselected(self):
        self.selected = False
        self.image = dict['test']
    
    def move_char(self, pos, can_move=True):
        if can_move:
            self.char_unselected()
            self.moved = True
            self.image = dict['test_moved']
            self.char_x_pos = pos[0] + self.map_x_offset
            self.char_y_pos = pos[1] + self.map_y_offset
            self.update_rect()

    def reset_move(self):
        self.selected = False
        self.moved = False
        self.image = dict['test']

    def update_rect(self):
        self.char_x_onscreen = self.char_x_pos-self.map_x_offset
        self.char_y_onscreen = self.char_y_pos-self.map_y_offset
        self.rect = (self.char_x_onscreen*32,self.char_y_onscreen*32)

if __name__ == "__main__":
    test = character('test',[25,25])
    print(test.id,test.char_x_pos,test.char_y_pos)

    HEIGHT = 640    
    WIDTH = 640
    screen = pygame.display.set_mode((WIDTH,HEIGHT))


    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(test.image,test.rect)
        print(test.rect)
        pygame.display.update()
        