import sys
import pygame
from pygame.locals import *
import terrain
import spritesheet
import func

ANIMATION_FRAME = 6
char_sheet = spritesheet.Spritesheet("Assets\img\Character\\test_char.png")
ross_sheet = spritesheet.Spritesheet("Assets\img\Character\FE8_Ross.png")

class Character(pygame.sprite.Sprite):
    def __init__(self,character_id:str,char_pos:list[int,int],map_offset:list[int,int]) -> None:
        super().__init__()
        self.id =  character_id

        #character and sprite position
        self.char_x_pos = char_pos[0]
        self.char_y_pos = char_pos[1]
        self.map_x_offset = map_offset[0]
        self.map_y_offset = map_offset[1]
        self.char_x_onscreen = self.char_x_pos-self.map_x_offset
        self.char_y_onscreen = self.char_y_pos-self.map_y_offset
        self.rect = (self.char_x_onscreen*32,self.char_y_onscreen*32)

        #animation
        self.still_image_set = [ross_sheet.parse_sprite("FE8_Ross_st1"),ross_sheet.parse_sprite("FE8_Ross_st2"),ross_sheet.parse_sprite("FE8_Ross_st3")]
        self.selected_image_set = [ross_sheet.parse_sprite("FE8_Ross_s1"),ross_sheet.parse_sprite("FE8_Ross_s2"),ross_sheet.parse_sprite("FE8_Ross_s3")]
        self.moved_image_set = [pygame.transform.grayscale(ross_sheet.parse_sprite("FE8_Ross_s1"))]
        self.image_set = self.still_image_set
        self.index = 0
        self.indexMax = len(self.image_set)
        self.current_frame = 0
        self.image = self.image_set[self.index]

        #movement
        self.selected = False
        self.moved = False
        self.movement = 5
    
    def pos_onscreen(self) -> tuple[int,int]:
        return (self.char_x_onscreen,self.char_y_onscreen)
    
    def char_pos(self) -> tuple[int,int]:
        return (self.char_x_pos,self.char_y_pos)
    
    def char_selected(self) -> None:
        self.selected = True
        self.image_set = self.selected_image_set
        self.reset_animation_counter()

    def char_unselected(self) -> None:
        self.selected = False
        self.image_set = self.still_image_set
        self.reset_animation_counter()
    
    def move_char(self, tile:terrain.Tile, destination:list[int,int]) -> None:
        if tile.can_move():
            self.char_unselected()
            self.moved = True
            self.image_set = self.moved_image_set
            self.reset_animation_counter()  
            self.char_x_pos = destination[0]
            self.char_y_pos = destination[1]
            self.update_rect()

    def reset_move(self) -> None:
        self.selected = False
        self.moved = False
        self.image_set = self.still_image_set
        self.reset_animation_counter()

    def update_rect(self) -> None:
        self.char_x_onscreen = self.char_x_pos-self.map_x_offset
        self.char_y_onscreen = self.char_y_pos-self.map_y_offset
        self.rect = (self.char_x_onscreen*32,self.char_y_onscreen*32)

    def update_sprite(self) -> None:
        func.update_animation(self,ANIMATION_FRAME)

    def reset_animation_counter(self) -> None:
        self.index = 0
        self.indexMax = len(self.image_set)
        self.current_frame = 0
        self.image = self.image_set[self.index]

if __name__ == "__main__":
    test = Character('test',[25,25])
    print(test.id,test.char_x_pos,test.char_y_pos)

    HEIGHT = 640    
    WIDTH = 640
    screen = pygame.display.set_mode((WIDTH,HEIGHT))


    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(test.image,test.rect)
        print(test.rect)
        pygame.display.update()
        