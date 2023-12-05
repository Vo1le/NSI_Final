import pygame
from pygame.locals import * #les librairies

pygame.init()
ecran = pygame.display.set_mode((0,0))
global lenght,width
lenght,width = ecran.get_size()
image_fond = pygame.image.load("attacker.jpg") #on definit le fond d'écran
nouvelle_image = pygame.transform.scale(image_fond, (lenght,width)) #et on le met à la taille de l'écran
ecran.blit(nouvelle_image,(0,0))
pygame.display.flip()

continuer = True

image = pygame.image.load("play.png")
image = pygame.transform.scale(image, (lenght//4, width//6))
sortie = pygame.image.load("exit.png")
sortie = pygame.transform.scale(sortie, (lenght//5,width//12)) #on load les image et on les redimensionne

while continuer: # la boucle pour les evenements et autres

    ecran.blit(image, (lenght//1.65,width//1.5))
    ecran.blit(sortie, (lenght//20, width//12)) #on configure les positions des images
    cox , coy = pygame.mouse.get_pos() #on prend les coordonnées du curseur
    if cox > lenght//1.65 and cox < lenght//1.65+lenght//4 and coy > width//1.5 and coy < width//1.5+width//6: 
        if pygame.mouse.get_pressed()[0]: #encaderment (qui correspond aux images) et qu'on clique gauche,
            with open("Jeu NSi.py") as f: #on lance un autre programme
                exec(f.read())
    if cox > lenght//20 and cox < lenght//20+lenght//5 and coy > width//12 and coy < width//12+width//12:
        if pygame.mouse.get_pressed()[0]:
            continuer = False #et si on clique sur "exit, ça arrête la boucle while et ca arrete le jeu
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False #pour arrêter le jeu si on appuie sur échap
                
    pygame.display.update() #update ecran

pygame.quit()
