import pygame

ecran = pygame.display.set_mode((0,0))
image = pygame.image.load("pattern.png")
image = pygame.transform.scale(image, (200, 200))
chemin = pygame.image.load("bonchemin.png") #on uploade et on redimensionne les images

continuer = True

while continuer:
        for i in range (0,2000,200):
            for k in range (0,1200,200):
                ecran.blit(image, (i,k)) #on dispose les images d'herbe en ligne
        for m in range (0,1200,32):
            ecran.blit(chemin, (984,m)) #on rajoute le chemin
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
        pygame.display.update() #update ecran

pygame.quit()
