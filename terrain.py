import pygame
from pygame.locals import *

tile_dict ={
    'blue':pygame.image.load("Assets/img/Terrain/TestTile_1.png"),
    'green':pygame.image.load("Assets/img/Terrain/TestTile_2.png"),
}

terrain_lookup ={
    1:'blue',
    2:'green',
}

class tile(pygame.sprite.Sprite):
    def __init__(self,tile_type:int,x_pos:int,y_pos:int):
        super().__init__()
        self.type = tile_type
        if self.type == 1:
            self.image = tile_dict['green']
        else:
            self.image = tile_dict['blue']
        self.rect = (int(x_pos*32),int(y_pos*32))



if __name__ == "__main__":
    test = tile(1,1,1)
    print(test)