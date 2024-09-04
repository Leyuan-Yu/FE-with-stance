import pygame
from pygame.locals import *
from cursor import new_cursor
import sys

pygame.init()

HEIGHT = 640    
WIDTH = 640
X_tiles = int(WIDTH/32)
Y_tiles = int(HEIGHT/32)
FPS = 30

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

def move_cursor(boundary:list[int]):
    pressed_keys  = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        if new_cursor.x_pos > 0:
            new_cursor.move_left()
        else:
            new_cursor.x_pos = 0
            new_cursor.update_rect()
    if pressed_keys[K_RIGHT]:
        if new_cursor.x_pos < boundary[0]-1:
            new_cursor.move_right()
        else:
            new_cursor.x_pos = boundary[0]-1
            new_cursor.update_rect()
    if pressed_keys[K_UP]:
        if new_cursor.y_pos > 0:
            new_cursor.move_up()
        else:
            new_cursor.y_pos = 0
            new_cursor.update_rect()
    if pressed_keys[K_DOWN]:
        if new_cursor.y_pos < boundary[1]-1:
            new_cursor.move_down()
        else:
            new_cursor.y_pos = boundary[1]-1
            new_cursor.update_rect()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in range (20):
        for j in range (20):
            screen.blit(tile2,(x+x_offset*j, y+y_offset*i))
    screen.blit(new_cursor.image,new_cursor.rect)
    move_cursor([X_tiles,Y_tiles])
    pygame.display.update()
    print(new_cursor.cursor_pos())
    FramePerSec.tick(FPS)
