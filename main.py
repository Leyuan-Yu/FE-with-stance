import pygame
from pygame.locals import *
import sys

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
screen.fill((0,0,0))
pygame.display.set_caption("FE")

#TEST AREA
tile1 = pygame.image.load("Assets/img/Terrain/TestTile_1.png")
tile2 = pygame.image.load("Assets/img/Terrain/TestTile_2.png")

x = 0
y = 0
x_offset = 32
y_offset = 32

all_sprites = pygame.sprite.Group()

new_cursor = cursor.cursor()
all_sprites.add(new_cursor)

level1 = level.level(1,[40,40])
level1_map = level1.generate_map([20,20])

for tile in level1_map:
        screen.blit(tile.image,tile.rect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    level1.move_map(new_cursor.move_cursor([X_tiles,Y_tiles]),new_cursor.cursor_pos())
    #draw updated map:
    for tile in level1.map_tiles:
         screen.blit(tile.image,tile.rect)
    #draw sprites
    for sprite in all_sprites:
        sprite.update_sprite()
        screen.blit(sprite.image,sprite.rect)
    pygame.display.update()
    #print(new_cursor.cursor_pos())
    FramePerSec.tick(FPS)
