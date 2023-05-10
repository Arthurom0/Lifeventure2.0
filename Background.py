import pygame
from constants import *
from Personnage import Personnage
from momie import Momie
from Mechant import Mechant
import Jeu
pygame.init()
pygame.font.init() 
#Class du background 
class Background(pygame.sprite.Sprite):                         #Le fond qui est en mouvemet
    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran
        self.entites = []
        self.setImage(0)
        ecran = pygame.display.set_mode((width, height))
        self.hearts = [
                [1,2],
                [2,1]
        ]

        
    def display(self, camera_offset):
        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]
        self.ecran.blit(self.image, (pixel_x, pixel_y))
    
    def setImage(self, imageId):
        self.image = pygame.image.load(IMAGES_FOND[imageId])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        get_back = pygame.Surface((1, height))
        get_back.blit(self.image, (0, 0))
        get_back = pygame.transform.scale(get_back,(width, height))
        self.ecran.blit(get_back, (0, 0))

    def update(self):

        next





    def MOUV_MOMIE(self, momie, player) :
        if momie.rect.x < player.rect.x : 
            momie.move_right()
        if momie.rect.x > player.rect.x :
            momie.move_left()