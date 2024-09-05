import pygame
from pygame.locals import * 
import terrain

class level:
    def __init__(self,num:int,size:list[int,int],start_point=[0,0],screen_size=[20,20]):
        self.level_num = num
        self.size = size
        self.cursor_on_map = start_point
        self.screen_size = screen_size
        self.map_tiles = pygame.sprite.Group()

    def generate_map(self,screen_size:list[int,int]) ->pygame.sprite.Group:
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if j%2==0 or i%2==0:
                    new_tile = terrain.tile('blue',j,i)
                else:
                    new_tile = terrain.tile('green',j,i)
                self.map_tiles.add(new_tile)
        return self.map_tiles
    
    def move_map(self, direction:str, cursor_pos:tuple[int,int]) ->pygame.sprite.Group:
        print(self.cursor_on_map)
        #to handle cursing moving right
        if direction == 'right':
            self.cursor_on_map[0] +=1
        elif direction == 'right_scroll':
            if self.cursor_on_map[0] < self.size[0]-1:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0]-32, tile.rect[1])
                self.cursor_on_map[0] +=1
                return self.map_tiles
        #cursor moving left    
        if direction == 'left':
            self.cursor_on_map[0] -=1
        elif direction == 'left_scroll':
            if self.cursor_on_map[0] > 0:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0]+32, tile.rect[1])
                self.cursor_on_map[0] -=1
                return self.map_tiles 
        #cursor moving up 
        if direction == 'up':
            self.cursor_on_map[1] -=1
        elif direction == 'up_scroll':
            if self.cursor_on_map[1] > 0:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0], tile.rect[1]+32)
                self.cursor_on_map[1] -=1
                return self.map_tiles 
        #cursor moving down
        if direction == 'down':
            self.cursor_on_map[1] +=1
        elif direction == 'down_scroll':
            if self.cursor_on_map[1] < self.size[1]-1:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0], tile.rect[1]-32)
                self.cursor_on_map[1] +=1
                return self.map_tiles 
        else:
            return self.map_tiles