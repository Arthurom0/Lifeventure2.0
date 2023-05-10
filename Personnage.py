from constants import *
from game import *
import pygame
from utils import load_animation_images

#classe qui représente le personnage
class Personnage(pygame.sprite.Sprite):

    def __init__(self, ecran):
        super().__init__()
        self.ecran = ecran
        clock = pygame.time.Clock()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        #self.tick = pygame.time.Clock().tick(2)
        self. tick  = clock.tick(0)
        self.velocity_x = 30
        self.velocity_y = 5
        self.vitesse_x = 0
        self.vitesse_y = 0
        self.min_y = 666
        self.gravity = 1
        #self.velocity_z = 4
        self.image = pygame.image.load(ANIM_JEUNE)
        self.rect = self.image.get_rect()
        self.on_ground = True
        self.rect.x = 800
        self.rect.y = 666       
        self.min_y = 666

        self.current_image = 0
        self.animation = True
        self.images = {
            "marche_droite" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneD", (23 *2, 32*2)), 
            "idle" : load_animation_images(DOSSIER_ANIM_JEUNE, "JeuneIdle", (23 *2, 32 *2)),
            'marche_gauche' : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeuneG", (23 *2, 32 *2)),
            "saut_droite" : load_animation_images(DOSSIER_ANIM_JEUNE, "Saut_jeuneD", (32 *2, 32 *2)),
            "attaque_droite" : load_animation_images(DOSSIER_ANIM_JEUNE, "Jeune_attaqueD", (32 *2, 32 *2)),
            "saut_gauche" : load_animation_images(DOSSIER_ANIM_JEUNE, "Saut_jeuneG", (32 *2, 32 *2)),
            "attaque_gauche" : load_animation_images(DOSSIER_ANIM_JEUNE, "Jeune_attaqueG", (32 *2, 32 *2)),
        } 
        self.actuel = "idle" 
    # Afficher les animations (frames)        
    def display(self, camera_offset):
        self.current_image = self.current_image % len(self.images[self.actuel])

        pixel_x = self.rect.x + camera_offset[0]
        pixel_y = self.rect.y + camera_offset[1]

        self.ecran.blit(self.images[self.actuel][int(self.current_image)], (pixel_x, pixel_y))
        self.current_image += 1
    #fonction qui est activée lorsque le personnage ne bouge pas  
    def idle(self):
        self.actuel = "idle"
    #fonction qui est activée lorsque le personnage bouge vers la droite
    def move_right(self, container):
        """
        container est une liste [x, y] qui contient la largeuyr et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "marche_droite"
        self.rect.x += self.velocity_x
        # marge de 64 sur lequel le joueur ne peut pas aller a droite
        if self.rect.x > container[0] - 64 :
            self.rect.x = container[0] - 64 
        #fonction qui est activée lorsque le personnage bouge vers la gauche 
    def move_left(self, container):
        """
        container est une liste [x, y] qui contient la largeur et la hauteur de la map dans laquelle est le joueur (pour pas qu'il sorte)
        """
        self.actuel = "marche_gauche"
        self.rect.x -= self.velocity_x
        if self.rect.x < 64:
            self.rect.x = 64
    #fonction qui permet de sauter vers la droite
    def jumpD(self):
        self.actuel = "saut_droite"
        if self.vitesse_y == 0:
            self.vitesse_y = -10
    #fonction qui permet de faire sauter le personnage vers la gauche 
    def jumpG(self):
        self.actuel = "saut_gauche"
        if self.vitesse_y == 0:
            self.vitesse_y = -10
    #fonction qui permet de faire une attaque vers la droite 
    def attaqueD(self):
        self.actuel = "attaque_droite"

    #fonction qui permet de faire une attaque vers la gauche         
    def attaqueG(self):
        self.actuel = "attaque_gauche"
        
    def update(self):
        self.actuel = "saut_droite" or "saut_gauche"
        self.rect.y += self.vitesse_y
        self.vitesse_y += 0.7
        
        if self.rect.y >= self.min_y:
            self.vitesse_y = 0        
            self.rect.y = self.min_y


