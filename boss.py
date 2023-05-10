from constants import *
import pygame
from utils import load_animation_images
import time

#classe qui s'occupe du boss qui doit s'afficher que dans la map 3

class Boss(pygame.sprite.Sprite) :
    def __init__(self, ecran) :
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(BOSS)
        self.rect = self.image.get_rect()
        self.rect.x = 2650
        self.rect.y = 600
        self.current_image = 0
        self.animation = True 
        self.start_frame = time.time()
        self.noi = 16
        self.frames_per_second = 5   
        self.clock = pygame.time.Clock()
        self.delta_T = self.clock.tick(3) 

        self.images = {
            'idle' : load_animation_images(ENNNEMI_BOSS, "Boss_Idle", (128*2, 128*2)),
            'boss_atk' : load_animation_images(ENNNEMI_BOSS,"Boss_atk", (128*2, 128*2))
        }

        self.actuel  = "idle"
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        #self.current_image = int((time.time() - self.start_frame) * self.frames_per_second % self.noi)
        self.pixel_x = self.rect.x + camera_offset[0]
        self.pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (self.pixel_x, self.pixel_y))
        self.current_image += 1

    def update(self) :
        pass
    
    
    
    def atk(self, ecran, player, camera_offset) :
        self.actuel = "boss_atk"
        pygame.draw.line(ecran, (220,20,60), (player.rect.x+camera_offset[0]+32, player.rect.y+camera_offset[1]+16), (self.pixel_x + 60, self.pixel_y + 35), 4)

    def idle(self):
        self.actuel = "idle"
        