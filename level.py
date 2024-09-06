import pygame
from pygame.locals import * 
import terrain
import character

import random

class level:
    def __init__(self,level_id:int,level_data:dict,start_point=[0,0],screen_size=[20,20]):
        # level data and meta data
        self.level_id = level_id
        self.level_data = level_data
        self.size = (len(level_data['map'][0]),len(level_data['map']))
        self.screen_size = screen_size
        #key press and cursor
        self.cursor_on_map = start_point
        self.yes_last_pressed = []
        self.x_offset = start_point[0]
        self.y_offset = start_point[1] 
        # sprites
        self.map_tiles = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()

    def generate_map(self,screen_size:list[int,int]) ->pygame.sprite.Group:
        for row in enumerate(self.level_data['map']):
            for x_terrain in enumerate(row[1]):
                new_tile = terrain.tile(int(x_terrain[1]),x_terrain[0]-self.x_offset,row[0]-self.y_offset)
                self.map_tiles.add(new_tile)
        self.add_character()
        return self.map_tiles
    

    # handles cursor actions
    def level_action(self, key_press:str, cursor_pos:tuple[int,int]) ->pygame.sprite.Group:
        #print(self.cursor_on_map)
        #to handle cursing moving right
        if key_press == 'yes':
            if self.yes_last_pressed != cursor_pos:
                self.yes_last_pressed = cursor_pos
                print(f"yes at {self.cursor_on_map}")
        elif key_press == 'right':
            self.cursor_on_map[0] +=1
        elif key_press == 'right_scroll':
            self.right_scroll()
        #cursor moving left    
        elif key_press == 'left':
            self.cursor_on_map[0] -=1
        elif key_press == 'left_scroll':
            self.left_scroll()
        #cursor moving up 
        elif key_press == 'up':
            self.cursor_on_map[1] -=1
        elif key_press == 'up_scroll':
            self.up_scroll()
        #cursor moving down
        elif key_press == 'down':
            self.cursor_on_map[1] +=1
        elif key_press == 'down_scroll':
            self.down_scroll()
        else:
            return self.map_tiles
        
    def right_scroll(self):
        if self.cursor_on_map[0] < self.size[0]-1:
            for tile in self.map_tiles:
                tile.rect= (tile.rect[0]-32, tile.rect[1])
            self.cursor_on_map[0] +=1
            self.update_character_pos('right')
            return self.map_tiles    
        
    def left_scroll(self):
        if self.cursor_on_map[0] > 0:
            for tile in self.map_tiles:
                tile.rect= (tile.rect[0]+32, tile.rect[1])
            self.cursor_on_map[0] -=1
            self.update_character_pos('left')
            return self.map_tiles     
           
    def up_scroll(self):
        if self.cursor_on_map[1] > 0:
            for tile in self.map_tiles:
                tile.rect= (tile.rect[0], tile.rect[1]+32)
            self.cursor_on_map[1] -=1
            self.update_character_pos('up')
            return self.map_tiles 

    def down_scroll(self):
        if self.cursor_on_map[1] < self.size[1]-1:
            for tile in self.map_tiles:
                tile.rect= (tile.rect[0], tile.rect[1]-32)
            self.cursor_on_map[1] +=1
            self.update_character_pos('down')
            return self.map_tiles 


    # handles character related    
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
