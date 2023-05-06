import pygame
from constants import *
from utils import load_animation_images


class Momie(pygame.sprite.Sprite):
    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran 
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(ENNEMI_MOMIE)  # liste des images de la momie
        self.index = 0  # index de l'image actuelle dans la liste des images

        self.rect = self.image.get_rect()
        self.rect.x = 1580
        self.rect.y = 666
        self.current_image = 0
        self.animation = True


        self.vitesse_x = 0
        self.vitesse_y = 0

        self.velocity_x = 5  # vitesse de déplacement de la momie
        self.direction = 1  # direction de déplacement de la momie (1 pour droite, -1 pour gauche)

        self.images = {
            "momie_gauche": load_animation_images(DOSSIER_ENNEMI, "Momie_gauche", (32 * 2, 32 * 2)),
            "momie_droite": load_animation_images(DOSSIER_ENNEMI, "Momie_droite", (32 * 2, 32 * 2))
        
        }
        self.actuel = "momie_gauche"
    def idle(self):
        self.actuel = "momie_gauche"
        
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
        self.current_image += 1

    def move_right(self, container):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "momie_droite"
        self.rect.x += self.velocity_x
        # marge de 64 sur lequel le joueur ne peut pas aller a droite
        if self.rect.x > container[0] - 64 :
            self.rect.x = container[0] - 64 
        
    def move_left(self):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "marche_gauche"
        self.rect.x -= self.velocity_x
        if self.rect.x < 64:
            self.rect.x = 64



