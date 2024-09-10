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

class Tile(pygame.sprite.Sprite):
    def __init__(self,tile_type:int,x_pos:int,y_pos:int):
        super().__init__()

        #display related
        self.type = tile_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = (int(x_pos*32),int(y_pos*32))
   
        if self.type == 1:
            self.image = tile_dict['green']
            self.default_image = self.image
            self.resistance = 1
        else:
            self.image = tile_dict['blue']
            self.default_image = self.image
            self.resistance = 9

        #movement related
        self.occupied = False
        


    def return_xy(self) -> tuple[int,int]:
        return ((self.x_pos,self.y_pos))

    def set_travel(self):
        self.image = tile_dict['travel']

    def reset_tile_image(self):
        self.image = self.default_image

    def return_resistance(self, char='default'):
        return self.resistance
    
    def can_move(self) -> bool:
        if self.occupied == True:
            return False
        else:
            return True


if __name__ == "__main__":
    test = Tile(1,1,1)
    print(test)