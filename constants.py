import pygame
pygame.init()
BASE_DOSSIER = "res/"
IMAGES_FOND = [
    BASE_DOSSIER + "decors/Paysage3.png",
    BASE_DOSSIER + "decors/Map_Temple.png",
    BASE_DOSSIER + "decors/Paysage_4.png",
]
MUSIQUE_FOND = BASE_DOSSIER + "musiques/Morceau_sans_titre_1.mp3"
MUSIQUE_FOND1 = BASE_DOSSIER + "musiques/Musique_donjon.mp3"
MUSIQUE_FOND2 = BASE_DOSSIER + "musiques/Morceau_sans_titre_1.mp3"
DOSSIER_ANIM_JEUNE = BASE_DOSSIER + "anim_players/jeune/"
ANIM_JEUNE = DOSSIER_ANIM_JEUNE + "Jeune.png"
DOSSIER_ENNEMI = BASE_DOSSIER + "anim_players/cactus/"
ENNEMI_MOMIE =  BASE_DOSSIER + "anim_players/momie/"
MOMIE = ENNEMI_MOMIE + "momie_idle.png"
ENNEMI_CACTUS = DOSSIER_ENNEMI + "Cactus.png"
HEALTH = BASE_DOSSIER + "coeur/Coeur.png"
MENU = BASE_DOSSIER + "menu/menu.png"
DEATH  = BASE_DOSSIER + "Ecran_de_mort.png"
ENNNEMI_BOSS = BASE_DOSSIER + 'anim_players/Boss'
BOSS = ENNNEMI_BOSS + "/Boss_atk.png"
CINEMATIQUE = BASE_DOSSIER + '/Cinematique'
CINE = CINEMATIQUE + '/Cinematique_1.png'
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
DOSSIER_ANIM_BB = BASE_DOSSIER + "anim_players/bebe/"
DOSSIER_ANIM_VIEUX = BASE_DOSSIER + "anim_players/vieux"
BEBE = DOSSIER_ANIM_BB + 'bebe_idle_1.png'
VIEUX = DOSSIER_ANIM_VIEUX + 'Vieux_atk1.png'
