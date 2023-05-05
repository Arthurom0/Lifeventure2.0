import pygame
from constants import *
from utils import load_animation_images

class Mechant(pygame.sprite.Sprite):
    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(ENNEMI_CACTUS)
        self.rect = self.image.get_rect()
        self.rect.x = 1580
        self.rect.y = 666
        self.current_image = 0
        self.animation = True
        self.actuel = "idle_ennemi1" 
        self.images = {
            "idle_ennemi1" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32 * 2, 32 * 2)), 
        } 

    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
        self.current_image += 1
    
    def update(self):
        pass


        

    
