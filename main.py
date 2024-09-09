import pygame
from pygame.locals import *
import sys
import json
import func

import cursor
import level

pygame.init()

HEIGHT = 640    
WIDTH = 640
X_tiles = int(WIDTH/32)
Y_tiles = int(HEIGHT/32)
FPS = 30
ANIMATION_FRAME = 12

FramePerSec = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("FE")


x = 0
y = 0
x_offset = 32
y_offset = 32

all_sprites = pygame.sprite.Group()

#cursor
new_cursor = cursor.cursor()
all_sprites.add(new_cursor)

#level
level_data = func.load_level_data()
level1 = level.level(1,level_data['1'],level_data['1']['map_start'])
level1_map = level1.generate_map([20,20])
level1_char = level1.return_characters()
#new_cursor.set_cursor_pos([10,10])

#initialising the level by adding tiles and characters
for tile in level1_map:
        screen.blit(tile.image,tile.rect)
for char in level1_char:
     screen.blit(char.image,char.rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    level1.level_action(new_cursor.cursor_action([X_tiles,Y_tiles]),new_cursor.cursor_pos())
    #draw updated map:
    level1.map_tiles.draw(screen)
    #draw characters:
    level1_char.draw(screen)
    #draw sprites
    for sprite in all_sprites:
        sprite.update_sprite()
    all_sprites.draw(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)
