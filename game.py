#importer le module pygame
from playsound import playsound 
import pygame, sys
from os import listdir
from constants import *
from utils import load_animation_images
from Personnage import Personnage
from Background import Background
from Mechant import Mechant
from Jeu import *
from momie import Momie 
pygame.init()
pygame.font.init() 
def jeuprincipal():
    global vies
    jumping = True
    Y_gravity = 1
    JUMP_HEIGHT = 20
    Y_velocity = JUMP_HEIGHT 

  
    #fenêtre du jeu
    pygame.display.set_caption("Lifenture")
    ecran = pygame.display.set_mode((width, height))
    
    x_fond = 0
    y_fond = 0
    width_max = 1920
    height_max = 1080
    #taille
    taille = 2

    #Musique
    DO_PLAY_SOUND = False
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
        "momie" : load_animation_images(DOSSIER_ENNEMI, "Momie", (32, 32))
    } 

    #charger le personnage
    player = Personnage(ecran)
    cactus = Mechant(ecran)
    back = Background(ecran)
    momie = Momie(ecran)
    #charger le jeu
    game = Jeu()

    #vie du perso
    vies = 3
    
    # qui permet de savoir sur quelle map on est
    current_map_id = 0

    # liste qui va conteir les truc a afficher (fond, mobs, joueur, items...)
    entities = [back, player, cactus, momie]

    # placement de la caméra qu'on peut déplacer indépendamenr du joueur
    camera_offset = [0, 0]

    """#Change la map/ place la map
    def set_nd_map():
        global current_map_id
        camera_offset[0] = 0
        camera_offset[1] = 0
        current_map_id = 1
        player.rect.x = 0
        player.rect.y = 900
        back.setImage(1)
        player.min_y = 900"""
        

    # tant que le jeu est en marche...
    main_window = True 
    while main_window == True :


        #delta temps
        delta_t = clock.tick(30)

        # mettre à jour l'écran
   


        

        #fermeture de la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_window = False


            # defini si la touche est appuyée ou non (a faire avant de detecter les touches)
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            #    
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
        
        #fonts :
        my_font = pygame.font.SysFont('Comic Sans MS', 30, True)





        if vies == 0 :
            return vies
            
            
            
        
        for entity in entities:
            entity.update()

        # déplacement du personnage et mechant
        player.idle()  
        #momie.idle()
        if player.vitesse_y != 0 and player.rect.x < player.velocity_x:
            player.jumpD() or player.jumpG()
        if player.vitesse_y > 0 or player.vitesse_y < 0 :
            player.actuel =  "saut_droite" or "saut_gauche"
        if game.pressed.get(pygame.K_RIGHT):
            player.move_right([back.image.get_width(), back.image.get_height()])
        if game.pressed.get(pygame.K_LEFT):
            player.move_left([back.image.get_width(), back.image.get_height()])
        if game.pressed.get(pygame.K_UP) and player.actuel == "marche_droite":
            player.jumpD()
        if game.pressed.get(pygame.K_UP) and player.actuel == "idle":
            player.jumpD()
        if game.pressed.get(pygame.K_UP) and player.actuel == "marche_gauche":
            player.jumpG()
        if game.pressed.get(pygame.K_SPACE) and player.actuel == "marche_droite":
            player.attaqueD()
        if game.pressed.get(pygame.K_SPACE) and player.actuel == "marche_gauche":
            player.attaqueG()
        if game.pressed.get(pygame.K_SPACE) and player.actuel == "idle":
            player.attaqueD()
        if game.pressed.get(pygame.K_ESCAPE):
                pygame.quit()

        # on déplace la caméra sur le joueur



        #Montrer le personnage et mechant
        for entity in entities:
            entity.display(camera_offset)


        back.Portes(game, player, cactus, momie, ecran, camera_offset, width_max)
        
        #back.ANIM_COEUR(player, cactus, camera_offset, vies)

        # afficher les vies

        heart_image = pygame.image.load(HEALTH)
        def heart_imaging(x, y) :
            ecran.blit(heart_image, (x, y))

        
        #data box to follow conditions to take out hearts
        a = player.rect.x
        b = player.rect.y
        c = cactus.rect.x
        d = cactus.rect.y
        rect1 = player.hitbox = (player.rect.x+camera_offset[0] - 10, player.rect.y+camera_offset[1], 64, 64)
        rect2 = cactus.hitbox = (cactus.rect.x+camera_offset[0] - 10, cactus.rect.y+camera_offset[1], 64, 64)
        
        #print(a, b, c, d)
        
        if c - 20 <= a + 20 <= c + 20 or c + 20 >= a - 20 >= c or c+20 > a >c-20 :
            if d - 32 <= b + 32 <= d + 32 or d + 32 >= b - 32 >= d or d+32 > b >d-32 :
                vies -= 1
                back.LES_COEURS(player)
                                            
                
                
                print(vies)


                            
        print(vies)
            #animation des cœurs :
        if vies == 3 :
            heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+3, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+20, player.rect.y + camera_offset[1]-35)
        if vies == 2 :
            heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35), heart_imaging(player.rect.x + camera_offset[0]+3, player.rect.y + camera_offset[1]-35)
        else :
            heart_imaging(player.rect.x + camera_offset[0]-15, player.rect.y + camera_offset[1]-35)

        pygame.display.flip()

    #fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

jeuprincipal()
