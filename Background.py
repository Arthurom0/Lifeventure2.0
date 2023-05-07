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

    def Portes(self, game, player, cactus, momie, ecran, camera_offset, width_max) :
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                #   detect si le personnage appui sur une touche  
            elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
        #ordre = [map_id, xmin et max de player, rect.x de player……]
        self.portes = [
            [1, 2710, 2770, 700, 900, 1000, 1500, 750],
            [2, 3050, 3250, 700, 750, 700, 1500, 750], 
            [3, 3050, 3250, 0, 750, 700, 1500, 750]
        ]
        camera_offset[0] = -(player.rect.x - width_max//2)
        
        #ecran = pygame.display.set_mode((width, height))
            
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
                    if porte[0] > 1 :
                        if porte[5] >=  momie.rect.x : 
                            while not momie.rect.x == porte[6] :
                                momie.move_right()
                        if porte[6] == momie.rect.x :
                            while not momie.rect.x == porte[5] :
                                Momie.move_left()
                    if porte[0] == 0 :  
                        self.setImage(0)
                    if porte[1] == 1 :
                        self.setImage(1)
                    if porte[2] == 2 :
                        self.setImage(2)



    def ANIM_COEUR(self, player, cactus, camera_offset, heart_imaging, vies) : 
            a = player.rect.x
            b = player.rect.y
            c = cactus.rect.x
            d = cactus.rect.y
            rect1 = player.hitbox = (player.rect.x+camera_offset[0] - 10, player.rect.y+camera_offset[1], 64, 64)
            rect2 = cactus.hitbox = (cactus.rect.x+camera_offset[0] - 10, cactus.rect.y+camera_offset[1], 64, 64)
            
            print(a, b, c, d)
            
            if c - 20 <= a + 20 <= c + 20 or c + 20 >= a - 20 >= c or c+20 > a >c-20 :
                if d - 32 <= b + 32 <= d + 32 or d + 32 >= b - 32 >= d or d+32 > b >d-32 :

                    print(rect1, rect2) 
                    vies -= 1 
                    if vies == 2:
                        heart_imaging(1300, 10 )                                    
                        current_map_id = 0
                        player.rect.x = 0
                        player.rect.y = 666
                        self.setImage(0)
                        player.min_y = 666
                        cactus.rect.x = 1500
                        cactus.rect.y = 666
                        vies = 2
                    elif vies == 1:
                        current_map_id = 0
                        player.rect.x = 0
                        player.rect.y = 666
                        self.setImage(0)
                        player.min_y = 666
                        player.velocity_x = 13
                        player.velocity_y = 5
                        player.vitesse_x = 0
                        player.vitesse_y = 0
                        player.min_y = 666
                        cactus.rect.x = 1500
                        cactus.rect.y = 666
                        vies = 1
            #animation des cœurs :
            if vies == 3 :
                heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+3, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+20, player.rect.y + camera_offset[1]-35)
            elif vies == 2 :
                heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+3, player.rect.y + camera_offset[1]-35)
            else :
                heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35)
