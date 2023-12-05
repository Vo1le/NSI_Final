import pygame
from pygame.locals import*

pygame.mixer.init()
fenetre = pygame.display.set_mode((300,300))
 
son = pygame.mixer.Sound('Magenta Storm.mp3')
son.play(loops=-1, maxtime=0, fade_ms=0)

continuer = True

while continuer:
     for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                
pygame.quit()
