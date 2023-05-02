"""
fichier avec des fonctions utilitaires
"""

import pygame
from os import listdir
from constants import *

def load_img(path, size):
    """Charge une image et ajuste sa taille"""


    # Chargement de l'image
    img = pygame.image.load(path)
    

    # smoothscale() nécessite une image en 24-bits ou 32-bits
    if img.get_bitsize() in (24, 32):
        return pygame.transform.smoothscale(img, size)
    return pygame.transform.scale(img, size)


def load_animation_images(path, name, size):

    # On cherche tous les images dans les dossiers avec le nom et on charge avec une certaine taille 
    return [load_img(path + "/" + file, size) for file in listdir(path) if file.startswith(name)]

#Dictionnaire
animation = {
    "marche" : load_animation_images(DOSSIER_ANIM_JEUNE, "MarcheJeune", (32, 32)),
    "mechant" : load_animation_images(DOSSIER_ENNEMI, "Cactus", (32, 32)),
} 
