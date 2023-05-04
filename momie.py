import pygame
from constants import *
from utils import load_animation_images
momie1 = pygame.image.load("momie_walking1.png").convert_alpha()
momie2 = pygame.image.load("momie_walking2.png").convert_alpha()

class Momie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [momie1, momie2]  # liste des images de la momie
        self.index = 0  # index de l'image actuelle dans la liste des images
        self.image = self.images[self.index]  # image actuelle de la momie
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = 5  # vitesse de déplacement de la momie
        self.direction = 1  # direction de déplacement de la momie (1 pour droite, -1 pour gauche)

    def update(self):
        self.rect.x += self.velocity_x * self.direction
        self.index += 0.2  # vitesse de l'animation de la momie
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
