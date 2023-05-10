from playsound import playsound 
import pygame, sys
from os import listdir
from constants import *
from utils import load_animation_images
from Personnage import Personnage
from Background import Background
from Mechant import Mechant
from Jeu import * 
import time
from game import jeuprincipal
#from game import vies

#Bonjour 

pygame.init()
pygame.font.init() 
 #Bonjour 

screen = pygame.display.set_mode((1920,1080))

clock = pygame.time.Clock()

this = True
#pygame.draw.rect(screen, (255,255, 255), pygame.Rect(371, 332, 1095, 250))
game = Jeu()
while this == True :
    def main_menu() :
        pygame.display.set_caption("MENU")
        #BG = pygame.display.set_mode((width, height))
        #A = pygame.Rect(375, 330,1100, 240)
        #B = pygame.Rect((600, 725), (265, 100))
        menu = True
        Back = pygame.image.load(MENU)
        Back = pygame.transform.scale(Back, (1920, 1080))

        while menu == True  :#boucle principale
            screen.blit(Back, (0,0))
            Position_souris = pygame.mouse.get_pos()
            delta_t = clock.tick(60)
            font = pygame.font.Font('freesansbold.ttf', 32)

            text = font.render(f'{Position_souris}', True, (255, 125, 0))
            textRect = text.get_rect()
            textRect.center = (100, 100)
            screen.blit(text, textRect)

            for event in pygame.event.get():#quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    print(Position_souris)
                    if 735 < Position_souris[0] < 1090 and  645 < Position_souris[1] <  800:
                        return True
                    if 800 < Position_souris[0] < 1050 and  840 < Position_souris[1] <  940:
                        pygame.quit()
                        sys.exit()
            
            
            
            
            pygame.display.flip()
    
    def death_screen() :#ecran avec 2 optio apres mourir dans le jeu
        pygame.display.set_caption("DEATH_screen")
        #BG = pygame.display.set_mode(width, height)
        Death = pygame.image.load(DEATH)
        
        death = True
        
        while death == True :
            screen.blit(Death, (0,0))
            
            Position_souris = pygame.mouse.get_pos()
    
            delta_t = clock.tick(30)
        
            for event in pygame.event.get():#quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    #print(Position_souris)
                    if 772 < Position_souris[0] < 1175 and  645 < Position_souris[1] <  753:
                        return False
                    if 840 < Position_souris[0] < 1110 and  800 < Position_souris[1] <  916:
                        return True   
            pygame.display.flip()





    if main_menu() == True :#boucle qui permet de launch main menu puis import le jeu
        
        a = jeuprincipal()
 


    if a == 0 : 
        death_screen()
        pygame.display.flip()
    while True :
        if death_screen() == True :
            main_menu()
        #    pygame.display.flip()
            break
        if death_screen() == False :
            jeuprincipal()








for event in pygame.event.get():#quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
