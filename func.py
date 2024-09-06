import json
import pygame
from pygame.locals import *

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


if __name__ == "__main__":
    bind_key()
    print(pygame.K_UP)