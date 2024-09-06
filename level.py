import pygame
from pygame.locals import * 
import terrain
import character

import random

class level:
    def __init__(self,level_id:int,level_data:dict,start_point=[0,0],screen_size=[20,20]):
        self.level_id = level_id
        self.level_data = level_data
        self.size = (len(level_data['map'][0]),len(level_data['map']))
        self.cursor_on_map = start_point
        self.x_offset = start_point[0]
        self.y_offset = start_point[1] 
        self.screen_size = screen_size
        self.map_tiles = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()

    def generate_map(self,screen_size:list[int,int]) ->pygame.sprite.Group:
        for row in enumerate(self.level_data['map']):
            for x_terrain in enumerate(row[1]):
                new_tile = terrain.tile(int(x_terrain[1]),x_terrain[0]-self.x_offset,row[0]-self.y_offset)
                self.map_tiles.add(new_tile)
        self.add_character()
        return self.map_tiles
    
    def level_action(self, key_press:str, cursor_pos:tuple[int,int]) ->pygame.sprite.Group:
        #print(self.cursor_on_map)
        #to handle cursing moving right
        if key_press == 'right':
            self.cursor_on_map[0] +=1
        elif key_press == 'right_scroll':
            if self.cursor_on_map[0] < self.size[0]-1:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0]-32, tile.rect[1])
                self.cursor_on_map[0] +=1
                self.update_character_pos('right')
                return self.map_tiles
        #cursor moving left    
        if key_press == 'left':
            self.cursor_on_map[0] -=1
        elif key_press == 'left_scroll':
            if self.cursor_on_map[0] > 0:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0]+32, tile.rect[1])
                self.cursor_on_map[0] -=1
                self.update_character_pos('left')
                return self.map_tiles 
        #cursor moving up 
        if key_press == 'up':
            self.cursor_on_map[1] -=1
        elif key_press == 'up_scroll':
            if self.cursor_on_map[1] > 0:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0], tile.rect[1]+32)
                self.cursor_on_map[1] -=1
                self.update_character_pos('up')
                return self.map_tiles 
        #cursor moving down
        if key_press == 'down':
            self.cursor_on_map[1] +=1
        elif key_press == 'down_scroll':
            if self.cursor_on_map[1] < self.size[1]-1:
                for tile in self.map_tiles:
                    tile.rect= (tile.rect[0], tile.rect[1]-32)
                self.cursor_on_map[1] +=1
                self.update_character_pos('down')
                return self.map_tiles 
        else:
            return self.map_tiles
        
    def add_character(self):
        for i in range(10):
            new_c = character.character('test',[random.randint(0,39),random.randint(0,39)],[self.x_offset,self.y_offset]) 
            self.character_sprites.add(new_c)
    
    def return_characters(self) -> pygame.sprite.Group:
        return self.character_sprites

    def update_character_pos(self, key_press:str) -> pygame.sprite.Group:
        for char in self.character_sprites:
            if key_press == 'left':
                char.map_x_offset -= 1
                char.update_rect()
            if key_press == 'right':
                char.map_x_offset += 1
                char.update_rect()
            if key_press == 'up':
                char.map_y_offset -= 1
                char.update_rect()
            if key_press == 'down':
                char.map_y_offset += 1
                char.update_rect()
