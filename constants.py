import pygame
pygame.init()
BASE_DOSSIER = "res/"
IMAGES_FOND = [
    BASE_DOSSIER + "decors/Paysage3.png",
    BASE_DOSSIER + "decors/Map_Temple.png",
    BASE_DOSSIER + "decors/Paysage_4.png",
]
MUSIQUE_FOND = BASE_DOSSIER + "musiques/Musique_donjon.mp3"
DOSSIER_ANIM_JEUNE = BASE_DOSSIER + "anim_players/jeune/"
ANIM_JEUNE = DOSSIER_ANIM_JEUNE + "Jeune.png"
DOSSIER_ENNEMI = BASE_DOSSIER + "anim_players/cactus/"
ENNEMI_MOMIE = DOSSIER_ENNEMI + "momie_walking1.png"
ENNEMI_CACTUS = DOSSIER_ENNEMI + "Ennemi1_1.png"
HEALTH = BASE_DOSSIER + "coeur/Coeur.png"
MENU = BASE_DOSSIER + "menu/menu.png"
DEATH  = BASE_DOSSIER + "Ecran_de_mort.png"
#ENNMI_MOMI = BASE_DOSSIER +
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h

