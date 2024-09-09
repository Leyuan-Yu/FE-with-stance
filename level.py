import pygame
from pygame.locals import * 
import terrain
import character

import func
import random

class level:
    def __init__(self,level_id:int,level_data:dict,start_point=[0,0],screen_size=[20,20]):
        # level data and meta data
        self.level_id = level_id
        self.level_data = level_data
        self.size = (len(level_data['map'][0]),len(level_data['map']))
        self.screen_size = screen_size
        self.tile_pos_map = []
        #key press and cursor
        self.cursor_on_map = start_point
        self.yes_last_pressed = None
        self.x_offset = start_point[0]
        self.y_offset = start_point[1] 
        self.movable_tiles = []
        # sprites
        self.map_tiles = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()

    def generate_map(self,screen_size:list[int,int]) ->pygame.sprite.Group:
        for row in enumerate(self.level_data['map']):
            new_row = []
            for x_terrain in enumerate(row[1]):
                new_tile = terrain.tile(int(x_terrain[1]),x_terrain[0]-self.x_offset,row[0]-self.y_offset)
                self.map_tiles.add(new_tile)
                new_row.append(new_tile)
            self.tile_pos_map.append(new_row)
        self.add_character()
        return self.map_tiles

    # handles cursor actions
    def level_action(self, key_press:str, cursor_pos:tuple[int,int]) ->pygame.sprite.Group:
        #if menu is pressed execute end turn
        if key_press == 'menu':
            self.menu_pressed()
        #if no is pressed
        elif key_press == 'no':
            self.no_pressed()
        #if yes is pressed
        elif key_press == 'yes':
            #check for cursor movement
            self.yes_pressed(cursor_pos)
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
        
    #key press related
    def menu_pressed(self):
        self.end_turn()
    
    def no_pressed(self):
        #check for if a character is currently selected, if yes, unselect
        if selected_char := self.return_selected_char():
            selected_char.char_unselected()
            self.reset_tiles_default(self.movable_tiles)
            self.find_tile(selected_char.char_pos()).reset_tile_image()
            self.yes_last_pressed = None
    
    def yes_pressed(self, cursor_pos:tuple[int,int]):
        #check for cursor movement
        if self.yes_last_pressed != cursor_pos:
            self.yes_last_pressed = cursor_pos
            #if a char is selected
            if selected_char := self.return_selected_char():
                #if cursor is currently on another unmoved char, then switch selection
                if cursor_char := self.check_cursor_onChar(cursor_pos):
                    if not cursor_char.moved:
                        selected_char.char_unselected()
                        self.reset_tiles_default(self.movable_tiles)
                        cursor_char.char_selected()
                        self.movable_tiles = func.find_movable_tiles(cursor_char,self)
                        self.set_tiles_movable(self.movable_tiles)
                #else if the cursor is not on a character
                elif self.find_tile(self.cursor_on_map) in self.movable_tiles:
                    self.find_tile(selected_char.char_pos()).reset_tile_image()
                    self.reset_tiles_default(self.movable_tiles)
                    selected_char.move_char(self.find_tile(self.cursor_on_map))
                    self.movable_tiles = []
                    self.yes_last_pressed = None
            #if currently no char selected
            else:
                #check for cursor on char
                if cursor_char := self.check_cursor_onChar(cursor_pos):
                    #if that char has not moved
                    if not cursor_char.moved:
                        self.find_tile(cursor_char.char_pos()).set_travel()
                        self.movable_tiles = func.find_movable_tiles(cursor_char,self)
                        self.set_tiles_movable(self.movable_tiles)
                        cursor_char.char_selected()        
    
    def set_tiles_movable(self,tiles:list[terrain.tile]):
        for tile in tiles:
            tile.set_travel()
    def reset_tiles_default(self,tiles:list[terrain.tile]):
        for tile in tiles:
            tile.reset_tile_image()

    #map scrollling
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

    #handle tile related
    def find_tile(self, xy_onmap:list[int,int]) -> terrain.tile:
        return self.tile_pos_map[xy_onmap[1]][xy_onmap[0]]
    

    # handles character related    
    def add_character(self):
        for i in range(10):
            new_c = character.character('test',[random.randint(20,39),random.randint(20,39)],[self.x_offset,self.y_offset]) 
            self.character_sprites.add(new_c)
    
    def return_characters(self) -> pygame.sprite.Group:
        return self.character_sprites

    def return_selected_char(self) -> character.character:
        for char in self.character_sprites:
            if char.selected == True:
                return char
            
    def return_char_positions(self) -> list:
        pos_list = []
        for char in self.character_sprites:
            pos_list.append(char.char_pos())
        return pos_list
    
    def check_cursor_onChar(self,cursor_pos) -> character.character:
        for char in self.character_sprites:
            if char.pos_onscreen() == cursor_pos:
                return char

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


    # handles player end turn
    def end_turn(self):
        self.yes_last_pressed = None
        for char in self.character_sprites:
            char.reset_move()