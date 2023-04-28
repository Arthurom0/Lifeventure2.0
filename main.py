#importer le module pygame
from playsound import playsound 
import time
import pygame
from os import listdir
from constants import *
from utils import load_animation_images
from Personnage import Personnage
from Background import Background
from Mechant import Mechant
from Jeu import Jeu

pygame.init()
pygame.font.init() 

jumping = False
Y_gravity = 1
JUMP_HEIGHT = 20
Y_velocity = JUMP_HEIGHT 


#fenêtre du jeu
pygame.display.set_caption("Lifenture")
ecran = pygame.display.set_mode((width, height))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
x_fond = 0
y_fond = 0
width_max = 1920
height_max = 1080
#taille
taille = 2
#Musique

DO_PLAY_SOUND = True
if DO_PLAY_SOUND:
    pygame.mixer.music.load(MUSIQUE_FOND)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    
#Temps
clock = pygame.time.Clock()

#Dictionnaire
animation = {
    "marche" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeune", (32, 32)),
    "mechant" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32, 32)),
} 

#charger le personnage
player = Personnage(ecran)
cactus = Mechant(ecran)
back = Background(ecran)
#charger le jeu
game = Jeu()




# qui permet de savoir sur quelle map on est
current_map_id = 0

# liste qui va conteir les truc a afficher (fond, mobs, joueur, items...)
entities = [back, player, cactus]

# placement de la caméra qu'on peut déplacer indépendamenr du joueur
camera_offset = [0, 0]

#Change la map/ place la map
def set_nd_map():
    global current_map_id
    camera_offset[0] = 0
    camera_offset[1] = 0
    current_map_id = 1
    player.rect.x = 0
    player.rect.y = 900
    back.setImage(1)
    player.min_y = 900


# tant que le jeu est en marche...
running = True
while running:

    #delta temps
    delta_t = clock.tick(60)

    # mettre à jour l'écran
    pygame.display.flip()

    #fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # defini si la touche est appuyée ou non (a faire avant de detecter les touches)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    for entity in entities:
        entity.update()

    # déplacement du personnage et mechant
    player.idle()  
    
    if game.pressed.get(pygame.K_RIGHT):
        player.move_right([back.image.get_width(), back.image.get_height()])
    elif game.pressed.get(pygame.K_LEFT):
        player.move_left([back.image.get_width(), back.image.get_height()])

    if game.pressed.get(pygame.K_UP): 
        player.jump()
    if game.pressed.get(pygame.K_SPACE): 
        player.jump()
    if game.pressed.get(pygame.K_ESCAPE):
            pygame.quit()
        

    # on déplace la caméra sur le joueur
    camera_offset[0] = -(player.rect.x - width_max//2)
  

    #Montrer le personnage et mechant
    for entity in entities:
        entity.display(camera_offset)  
  
    # afficher les coordonnées (x;y du joueur)
    text_surface = my_font.render(f"x={player.rect.x}, y={player.rect.y}", False, (0, 0, 0))
    ecran.blit(text_surface, (0, 0))
    """text_surface = my_font.render(f"x={Mechant.rect.x}, y={Mechant.rect.y}", False, (0, 0, 0))
    ecran.blit(text_surface, (0, 0))"""
    # si la map est 1 et que le joueur est a droite
    if current_map_id == 0 and player.rect.x >= 2710 and player.rect.x <= 2770 :
        text_surface = my_font.render(f"Press down to enter", False, (0, 0, 0))
        ecran.blit(text_surface, (player.rect.x + camera_offset[0] - 100, 600))
        if game.pressed.get(pygame.K_RETURN):
            camera_offset[0] = 0
            camera_offset[1] = 0
            current_map_id = 1
            player.rect.x = 0
            player.rect.y = 900
            cactus.rect.x = 400
            cactus.rect.y = 900
            #ENNEMI_CACTUS.rect.x = 0
            #ENNEMI_CACTUS.rect.y = 900
            back.setImage(1)
            player.min_y = 900

    elif current_map_id == 1 and 3050 <= player.rect.x <= 3250 :
        text_surface = my_font.render(f"Press down to enter", False, (0, 0, 0))
        ecran.blit(text_surface, (player.rect.x + camera_offset[0] - 100, 600))
        if game.pressed.get(pygame.K_RETURN):
            camera_offset[0] = 0
            camera_offset[1] = 0
            current_map_id = 2
            player.rect.x = 0
            player.rect.y = 900
            back.setImage(2)
            player.min_y = 900

    a = player.rect.x
    b = player.rect.y
    c = cactus.rect.x
    d = cactus.rect.y
    rect1 = player.hitbox = (player.rect.x+camera_offset[0] - 10, player.rect.y+camera_offset[1], 64, 64)
    rect2 = cactus.hitbox = (cactus.rect.x+camera_offset[0] - 10, cactus.rect.y+camera_offset[1], 64, 64)
    
    print(a, b, c, d)
    
    if c - 32 <= a + 32 <= c + 32 or c + 32 >= a - 32 >= c or c+32 > a >c-32 :
        if d - 32 <= b + 32 <= d + 32 or d + 32 >= b - 32 >= d or d+32 > b >d-32 :
            pygame.draw.rect(ecran, (255,10, 10), player.hitbox,1)  
            pygame.draw.rect(ecran, (255,255, 255), cactus.hitbox,1)
            print(rect1, rect2)
            
    
    
        

    