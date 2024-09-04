import pygame
from pygame.locals import *

tile_dict ={
    'blue':pygame.image.load("Assets/img/Terrain/TestTile_1.png"),
    'green':pygame.image.load("Assets/img/Terrain/TestTile_2.png"),
}

class tile(pygame.sprite.Sprite):
    def __init__(self,tile_type:str,x_pos:int,y_pos:int):
        super().__init__()
        self.type = tile_type
        self.image = tile_dict[self.type]
        self.rect = (int(x_pos*32),int(y_pos*32))
