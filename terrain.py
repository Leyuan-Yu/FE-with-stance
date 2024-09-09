import pygame
from pygame.locals import *

tile_dict ={
    'blue':pygame.image.load("Assets/img/Terrain/TestTile_1.png"),
    'green':pygame.image.load("Assets/img/Terrain/TestTile_2.png"),
    'travel':pygame.image.load("Assets/img/Terrain/TestTile_0.png"),
}

terrain_lookup ={
    1:'blue',
    2:'green',
    0:'travel',
}

class tile(pygame.sprite.Sprite):
    def __init__(self,tile_type:int,x_pos:int,y_pos:int):
        super().__init__()
        self.type = tile_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        if self.type == 1:
            self.image = tile_dict['green']
            self.default_image = self.image
        else:
            self.image = tile_dict['blue']
            self.default_image = self.image
        self.rect = (int(x_pos*32),int(y_pos*32))

    def return_xy(self) -> tuple[int,int]:
        return ((self.x_pos,self.y_pos))

    def set_travel(self):
        self.image = tile_dict['travel']

    def reset_tile_image(self):
        self.image = self.default_image


if __name__ == "__main__":
    test = tile(1,1,1)
    print(test)