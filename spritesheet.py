import pygame
from pygame.locals import *
import json

class Spritesheet:
    def __init__(self, path) -> None:
        self.path = path
        self.meta_data = self.path.replace('png','json')
        self.sprite_sheet =  pygame.image.load(path)
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x ,y, w, h) -> pygame.Surface:
        sprite = pygame.Surface((w,h)) 
        sprite.set_colorkey((255,255,255))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite
    
    def parse_sprite(self, name) -> pygame.Surface:
        sprite = self.data['frames'][name]['frame']
        x,y,w,h = sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image = self.get_sprite(x,y,w,h)
        return image


if __name__ == "__main__":
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
    
    my_terrain = Spritesheet("Assets\img\Character\\test_char.png")
    char1 = my_terrain.parse_sprite("test_char_moved")

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for j in range(X_tiles):
            for i in range(Y_tiles):
                screen.blit(char1,(i*32,j*32))
        pygame.display.update()