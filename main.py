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

pygame.init()
pygame.font.init() 
 

screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("menu")

Back = pygame.image.load(MENU)
Back = pygame.transform.scale(Back, (1920, 1080))
clock = pygame.time.Clock()


pygame.draw.rect(screen, (255,255, 255), pygame.Rect(371, 332, 1095, 250))
game = Jeu()

def main_menu() :
    pygame.display.set_caption("MENU")
    BG = pygame.display.set_mode((width, height))
    #A = pygame.Rect(375, 330,1100, 240)
    #B = pygame.Rect((600, 725), (265, 100))
    menu = True


    while menu == True  :#boucle principale
        screen.blit(Back, (0,0))
        Position_souris = pygame.mouse.get_pos()
        delta_t = clock.tick(60)
        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render(f'{Position_souris}', True, (255, 125, 0))
        textRect = text.get_rect()
        textRect.center = (100, 100)
        screen.blit(text, textRect)
        #pygame.draw.rect(screen, ( 123,123,123 ),A,  width=10)
        #pygame.draw.rect(screen, ( 123,123,123 ),B,  width=10)
        
        for event in pygame.event.get():#quit
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                print(Position_souris)
                if 600 < Position_souris[0] < 865 and  725 < Position_souris[1] <  825:
                    return 1
                if 951 < Position_souris[0] < 1204 and  725 < Position_souris[1] <  825:
                    pygame.quit()
                    sys.exit()
        
        
        
        
        pygame.display.flip()

for i in range (0): 
    main_menu()
if main_menu() == 1 :
    print("hi")
    #PLAY()
    import game
        
for event in pygame.event.get():#quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()