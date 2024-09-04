import pygame
from pygame.locals import *
import cursor
import sys

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



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in range (20):
        for j in range (20):
            screen.blit(tile2,(x+x_offset*j, y+y_offset*i))
    new_cursor.move_cursor([X_tiles,Y_tiles])
    #draw sprites
    for sprite in all_sprites:
        sprite.update_sprite()
        screen.blit(sprite.image,sprite.rect)
    pygame.display.update()
    #print(new_cursor.cursor_pos())
    FramePerSec.tick(FPS)
