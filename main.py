import pygame
from pygame.locals import *
from cursor import new_cursor
import sys

pygame.init()

HEIGHT = 640    
WIDTH = 640
X_tiles = int(WIDTH/32)
Y_tiles = int(HEIGHT/32)
FPS = 60

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

def move_cursor():
    pressed_keys  = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        new_cursor.move_left
        print('left')
    if pressed_keys[K_RIGHT]:
        new_cursor.move_right
    if pressed_keys[K_UP]:
        new_cursor.y_pos -= 1
        print('up')
    if pressed_keys[K_DOWN]:
        new_cursor.y_pos += 1
        print('down')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in range (20):
        for j in range (20):
            screen.blit(tile2,(x+x_offset*j, y+y_offset*i))
    screen.blit(new_cursor.image,new_cursor.rect)
    move_cursor()
    pygame.display.update()
    FramePerSec.tick(FPS)
