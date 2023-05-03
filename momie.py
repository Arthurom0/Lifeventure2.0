import pygame
from constants import *
from utils import load_animation_images
class momie(pygame.sprite.Sprite):
    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(ENNEMI_CACTUS)
        self.rect = self.image.get_rect()