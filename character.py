import sys
import pygame
from pygame.locals import *

dict = {
    'test': pygame.image.load('Assets/img/Character/C_test.png'),
    'test_selected': pygame.image.load('Assets/img/Character/c_test_select.png')
}

class character(pygame.sprite.Sprite):
    def __init__(self,character_id:str,char_pos:list[int,int],map_offset:list[int,int]):
        super().__init__()
        self.id =  character_id
        self.char_x_pos = char_pos[0]
        self.char_y_pos = char_pos[1]
        self.map_x_offset = map_offset[0]
        self.map_y_offset = map_offset[1]

        self.image = dict['test']
        self.rect = ((self.char_x_pos-self.map_x_offset)*32,(self.char_y_pos-self.map_y_offset)*32)
        print(f"character created, with {self.image} at {self.rect}")

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
        