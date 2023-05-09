from constants import *
import pygame
from utils import load_animation_images

#classe qui s'occupe du boss qui doit s'afficher que dans la map 3

class Boss(pygame.sprite.Sprite) :
    def __init__(self, ecran) :
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(ENNEMI_CACTUS)
        self.rect = self.image.get_rect()
        self.rect.x = 2300
        self.rect.y = 600
        self.current_image = 0
        self.animation = True 
        

        self.images = {
            'idle' : load_animation_images(ENNNEMI_BOSS, "Boss_Idle", (128*2, 128*2)),
            'boss_atk' : load_animation_images(ENNNEMI_BOSS,"Boss_atk", (128*2, 128*2))
        }

        self.actuel  = "idle"
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
        self.current_image += 1

    def update(self) :
        pass
    
    
    
    def atk(self, ecran, player, camera_offset) :

        self.actuel = "boss_atk"
        pygame.draw.line(ecran, (220,20,60), (player.rect.x+camera_offset[0]+32, player.rect.y+camera_offset[1]+16), (2300, 600), 4)