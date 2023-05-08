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
        self.x_mouvement_momie = [1000, 1400]
        
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

    def Portes(self, smt,  game, player, cactus, momie, ecran, camera_offset, width_max) :
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                #   detect si le personnage appui sur une touche  
            elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
        #ordre = [map_id, xmin et max de player, rect.x de player……]
        self.portes = [
            [1, 2710, 2770, 600, 900, 1000, 1500, 750, 0],
            [2, 2710, 2770, 600, 900, 1000, 1500, 750, 1], 
            [2, 3050, 3250, 0, 750, 700, 1500, 750, 1]
        ]
        camera_offset[0] = -(player.rect.x - width_max//2)
        
        #fonction qui permet de actualiser les coordonées des sprites dans le jeu quand le personnage change de map en cliquant sur return lorsqu'il est devant la porte
        for porte in self.portes :
            
            if player.rect.x >= porte[1]  and  player.rect.x <= porte[2]:
                my_font = pygame.font.SysFont('Comic Sans MS', 30, True)
                text_surface = my_font.render(f"Appuyez sur enter pour enter", False, (0, 0, 0))
                ecran.blit(text_surface, (player.rect.x + camera_offset[0] - 100, 600))                
                if game.pressed.get(pygame.K_RETURN) : 
                    camera_offset[0] = 0
                    camera_offset[1] = 0   
                    current_map_id = porte[0]
                    self.setImage(porte[0])            
                    player.rect.x =  porte[3]
                    cactus.rect.x = porte[4]
                    player.min_y = porte[7]
                    cactus.rect.y = porte[7]
                    momie.rect.x = porte[5]
                    momie.rect.y = porte[7]

                    if porte[0] == 0 :  
                        self.setImage(0)
                    if porte[1] == 1 :
                        self.setImage(1)
                    if porte[2] == 2 :
                        self.setImage(2)


    #fonction que permet de placer les sprites au début de la game
    def START(self, player, cactus, momie):
        
        #attribus de la map/ backrgound appelé back dans game.py
        current_map_id = 0
        self.setImage(0)

        #attribus donnés au personnnages pricipal tel que la vitesse et les coordonées généraux qui sont reset lorques le personnage meurs
        player.rect.x = 0
        player.rect.y = 666       
        player.min_y = 666
        player.velocity_x = 13
        player.velocity_y = 5
        player.vitesse_x = 0
        player.vitesse_y = 0

        #coordonées de ennemis : cactus et momies
        cactus.rect.x = 1500
        cactus.rect.y = 666
        momie.rect.x = 1789 
        momie.rect.y = 666

    #fonction qui permet de supprimer des vies au personnage au fur et a mesure de la partie  
    def LES_COEURS(self, player, cactus, momie ) : #permet de afficher les coeurs

        #attribus de la map/ backrgound appelé back dans game.py
        current_map_id = 0
        self.setImage(0)

        #attribus donnés au personnnages pricipal tel que la vitesse et les coordonées généraux qui sont reset lorques le personnage meurs
        player.rect.x = 0
        player.rect.y = 666       
        player.min_y = 666
        player.velocity_x = 13
        player.velocity_y = 5
        player.vitesse_x = 0
        player.vitesse_y = 0

        #coordonées de ennemis : cactus et momies
        cactus.rect.x = 1500
        cactus.rect.y = 666
        momie.rect.x = 1789 
        momie.rect.y = 666
    
    
    
    
    



    def MOUV_MOMIE(self, momie) :
        if momie.rect.x > 900: 
            momie.move_left()
        
        if momie.rect.x < 1000 : 
            momie.move_right()