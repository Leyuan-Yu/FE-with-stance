import json
import pygame
from pygame.locals import *
import terrain
import character
import level

# load level data
def load_level_data() -> dict:
    with open("Assets/map/level_maps.json",'r') as json_map_data:
        data = json.load(json_map_data)
    return data

# handles key binding
# translating str into pygame key constant
key_map ={
    "K_UP":pygame.K_UP,
    "K_DOWN":pygame.K_DOWN,
    "K_LEFT":pygame.K_LEFT,
    "K_RIGHT":pygame.K_RIGHT,
    "K_a":pygame.K_a,
    "K_b":pygame.K_b,
    "K_c":pygame.K_c,
    "K_d":pygame.K_d,
    "K_e":pygame.K_e,
    "K_f":pygame.K_f,
    "K_g":pygame.K_g,
    "K_h":pygame.K_h,
    "K_i":pygame.K_i,
    "K_j":pygame.K_j,
    "K_k":pygame.K_k,
    "K_l":pygame.K_l,
    "K_m":pygame.K_m,
    "K_n":pygame.K_n,
    "K_o":pygame.K_o,
    "K_p":pygame.K_p,
    "K_q":pygame.K_q,
    "K_e":pygame.K_r,
    "K_s":pygame.K_s,
    "K_t":pygame.K_t,
    "K_u":pygame.K_u,
    "K_v":pygame.K_v,
    "K_w":pygame.K_w,
    "K_x":pygame.K_x,
    "K_y":pygame.K_y,
    "K_z":pygame.K_z,
    "K_RETURN":pygame.K_RETURN,
}
def load_key_bind() -> dict:
    with open("config/config.json",'r') as json_config_data:
        data = json.load(json_config_data)
    return data["key_bind"]

def bind_key():
    key_bind = load_key_bind()
    global up_key
    up_key = key_map[key_bind['up_key']]
    global down_key
    down_key = key_map[key_bind['down_key']]
    global left_key
    left_key = key_map[key_bind['left_key']]
    global right_key
    right_key = key_map[key_bind['right_key']]
    global yes_key
    yes_key = key_map[key_bind['yes_key']]
    global no_key
    no_key = key_map[key_bind['no_key']]
    global menu_key
    menu_key = key_map[key_bind['menu_key']]

#find movable tiles for character on map
def find_movable_tiles(char:character.character,level:level.level) -> list[terrain.tile]:
    #finding postions and movement
    char_movement = char.movement
    char_pos = [char.char_pos()[0],char.char_pos()[1]]
    #setup map to find tiles
    level_map = level.tile_pos_map
    #initialising tile lists
    unchecked_tiles = [[level.find_tile(char_pos),char_movement]]
    movable_tiles = [level.find_tile(char_pos)]

    def check_tiles(unchecked_tiles, char) -> list[terrain.tile]: 
        """
        a recursive function that takes tiles, check sourouding tiles based on movement. 
        make ammendements to the rolling list of unchecked tiles.
        until all movable tiles are listed in movable tiles list. 
        """ 
        #get the first item from unchecked list
        tile = unchecked_tiles[0]
        #retrieve movement
        remaining_movement = tile[1]
        #define xy position
        tile_x = tile[0].return_xy()[0] + level.x_offset
        tile_y = tile[0].return_xy()[1] + level.y_offset
        #check against boundaries, add possible sourounding tiles into check
        sourouding_tiles = []
        if tile_y - 1 >= 0:
            tile_above = level_map[tile_y - 1][tile_x]
            sourouding_tiles.append(tile_above)
        if tile_y + 1 < level.size[1]:
            tile_below = level_map[tile_y + 1][tile_x]
            sourouding_tiles.append(tile_below)  
        if tile_x - 1 >= 0:
            tile_left = level_map[tile_y][tile_x - 1]
            sourouding_tiles.append(tile_left) 
        if tile_x + 1 < level.size[0]:
            tile_right = level_map[tile_y][tile_x + 1]
            sourouding_tiles.append(tile_right)   

        #check for sourouding tiles for movement - resistance
        def check_postion(movement, tile, movable_tiles, unchecked_tiles, char):
            #if a movable tile is found, add into both lists
            if movement -  tile.return_resistance(char) >= 0 and tile not in movable_tiles:
                movable_tiles.append(tile)
                unchecked_tiles.append([tile, movement -  tile.return_resistance(char)])
        for souround_tile in sourouding_tiles:
            check_postion(remaining_movement,souround_tile,movable_tiles,unchecked_tiles, char)
        #all sourouding check complete, remove centre tile from unchecked
        unchecked_tiles.remove(tile)
        #pass on all uncheck tiles, include the new addition
        return unchecked_tiles
    
    #keep checking until unchecked_tiles are exhausted
    while unchecked_tiles:
        check_tiles(unchecked_tiles, char)

    return movable_tiles



if __name__ == "__main__":
    print(True * True * False)