import pygame
from constants import *
from utils import load_animation_images


class Momie(pygame.sprite.Sprite):
    def __init__(self, ecran):
        super().__init__()
        self.alive = True
        self.ecran = ecran 
        self.tick = pygame.time.Clock().tick()
        self.image = pygame.image.load(MOMIE)  # liste des images de la momie
        self.image = pygame.transform.scale(self.image, (52, 66))
        self.index = 0  # index de l'image actuelle dans la liste des images

        self.rect = self.image.get_rect()
        self.rect.x = 1789 
        self.rect.y = 666
        self.current_image = 0
        self.animation = True


        self.vitesse_x = 0
        self.vitesse_y = 0

        self.velocity_x = 3  # vitesse de déplacement de la momie
        self.direction = 1  # direction de déplacement de la momie (1 pour droite, -1 pour gauche)

        self.images = {
            "momie_gauche": load_animation_images(ENNEMI_MOMIE, "momie_gauche", (26*2, 33*2)),
            "momie_droite": load_animation_images(ENNEMI_MOMIE, "momie_droite", (26*2, 33*2)),
            'momie_idle' : load_animation_images(ENNEMI_MOMIE, 'momie_idle', (26*2, 33*2))
        }

        self.actuel = "momie_idle"
        
    def idle(self):
        self.actuel = "momie_idle"
        
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
       # self.ecran.blit(self.image, (pixel_x, pixel_y))
        self.current_image += 0.3

    def move_right(self):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "momie_droite"
        self.rect.x += self.velocity_x


        
    def move_left(self):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "momie_gauche"
        self.rect.x -= self.velocity_x


    def update(self) :
        pass

