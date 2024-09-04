import pygame
from pygame.locals import * 
import terrain

class level:
    def __init__(self,num:int,size:list[int,int]):
        self.level_num = num
        self.size = size

    def generate_map(self,screen_size:list[int,int]) ->pygame.sprite.Group:
        map_tiles = pygame.sprite.Group()
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                new_tile = terrain.tile('green',j,i)
                map_tiles.add(new_tile)
        return map_tiles