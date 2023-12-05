import pygame
from pygame.locals import * #les librairies

pygame.font.init()
pygame.mixer.init()
ecran = pygame.display.set_mode(size=(0, 0)) # on crée le siplay de l'écan
color = (255,255,255) # on crée une couleur
ecran.fill(color)# on l'applique au fond

#variables de bases
continuer = True 
clock = pygame.time.Clock()
hover = False 
  
#variables des sprites
 
class t1(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("7.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = 200
        self.health = 5
        self.degat = 1
        self.cost = 300
        self.taken = 0
        self.takenbase = 1
        self.cooldown = 0
        self.cooldownorigin = 0
        self.mask = pygame.mask.from_surface(self.image)
    def coor(self):
        return self.rect.center
    
class t2(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("t3.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = 500
        self.health = 3
        self.degat = 5
        self.cost = 700
        self.taken = 0
        self.takenbase = 1
        self.cooldown = 0
        self.cooldownorigin = 1
        self.mask = pygame.mask.from_surface(self.image)
    def coor(self):
        return self.rect.center

class mur(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mur.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = 150
        self.health = 5
        self.degat = 0
        self.cost = 100
        self.taken = 0
        self.takenbase = 0
        self.cooldown = 0
        self.cooldownorigin = 0
        self.mask = pygame.mask.from_surface(self.image)
    def coor(self):
        return self.rect.center

class enemi1(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemi1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 5
        self.movtower = 0
        self.avancev = 50
        self.radius = 110
        self.cost = 300
        self.degat = 2
        self.mask = pygame.mask.from_surface(self.image)
    def avance(self):
        self.rect.centerx = self.rect.centerx + self.avancev
        self.rect.centery = self.rect.centery + self.movtower

class enemi2(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("e2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 10
        self.movtower = 0
        self.avancev = 50
        self.radius = 110
        self.cost = 500
        self.degat = 1
        self.mask = pygame.mask.from_surface(self.image)
    def avance(self):
        self.rect.centerx = self.rect.centerx + self.avancev
        self.rect.centery = self.rect.centery + self.movtower
        
class enemi3(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("e3.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 3
        self.movtower = 0
        self.avancev = 50
        self.radius = 110
        self.cost = 500
        self.degat = 3
        self.mask = pygame.mask.from_surface(self.image)
    def avance(self):
        self.rect.centerx = self.rect.centerx + self.avancev
        self.rect.centery = self.rect.centery + self.movtower

class projectile(pygame.sprite.Sprite):
    def __init__(self, width, height,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pierre.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10
        self.angle = 1
        self.place = 0
        self.target = mur
        self.localtimecheck = 5
        self.mask = pygame.mask.from_surface(self.image)
    def avance(self):
        self.rect.centerx = self.rect.centerx + (self.speed)
        self.rect.centery = self.rect.centery + (self.angle)

     
#définition object jeu sprites

object_ = t1(1000, 1000, 200 , 300) #variables sprites
object_.rect.x = 200
object_.rect.y = 300
souris = pygame.sprite.Group()
placed = pygame.sprite.Group()
sr_ = t1(1000, 1000, 200, 300)
sr2_ = t2(1000, 1000, 200, 300)
sr3_ = mur(1000, 1000, 200, 300)
enemi1_ = enemi1(1000, 1000, 200, 300)
enemi2_ = enemi2(1000, 1000, 200, 300)
enemi3_ = enemi3(1000, 1000, 200, 300)
bullet_ = projectile(1000, 1000, 200, 300)

#variables fonctionnement sprites
sprtls = [0] 
cox = 0
coy = 0
black = (0,0,0)
vie_mur = 1

#variables temps
localtime = 5
timelcl = 60
change = 0

#variables argents et selection joueur
selectione = 1
money = 5000
joueur = 1
rad = 0
mouse_over = False

#variables et déclaration textuels (affichage)

font = pygame.font.Font(None, 64)
textjoueur = font.render("Joueur 1", True, (10, 10, 10))
texttemps = font.render(str(localtime), True, (10, 10, 10))
textargent = font.render(str(money)+"$", True, (10, 10, 10))
textstats = font.render("", True, (10, 10, 10))
textposjoueur = textjoueur.get_rect(x=ecran.get_width() - ecran.get_width()+10, y=10)
textpostemps = texttemps.get_rect(x=ecran.get_width() - ecran.get_width()+10, y=60)
textposargent = textargent.get_rect(x=ecran.get_width() - ecran.get_width()+10, y=110)
textposstats = textstats.get_rect(x=ecran.get_width() - ecran.get_width()+10, y=160)


image_fond = pygame.image.load("fondherbe.png")
bdf = pygame.image.load("bdf.png") #on definit le fond d'écran
nouvelle_image = pygame.transform.scale(image_fond, (ecran.get_width(), ecran.get_height())) #et on le met à la taille de l'écran

son = pygame.mixer.Sound('msc.mp3')
son.play(loops=-1, maxtime=0, fade_ms=0)


while continuer: # la boucle pour les evenements et autres
    
    change = change + 1
    sr_.rect.center = pygame.mouse.get_pos()
    sr2_.rect.center = pygame.mouse.get_pos()
    sr3_.rect.center = pygame.mouse.get_pos()
    enemi1_.rect.center = pygame.mouse.get_pos()
    enemi2_.rect.center = pygame.mouse.get_pos()
    enemi3_.rect.center = pygame.mouse.get_pos()

    #Timer -> fonctionnement
    
    if change >= timelcl: 
        change = 0
        localtime = localtime -1
        texttemps = font.render(str(localtime), True, (10, 10, 10))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if localtime == 0 and joueur == 1:
            textjoueur = font.render("Joueur 2", True, (10, 10, 10))
            joueur = 2
            change = 0
            localtime = 60
            money = 8000
            selectione = 1
            textstats = font.render("", True, (10, 10, 10))
            pygame.sprite.Group.empty(souris)
        elif localtime == 0 and joueur == 2:
            with open("ecran defender won.py") as f:
                exec(f.read())
        #détection dégats
        for z in placed:
            if type(z) is t1 or type(z) is t2 or type(z) is mur:
                for y in placed:
                    if type(y) is enemi1 or type(y) is enemi2 or type(y) is enemi3:
                                if y.rect.centerx + z.radius > z.rect.centerx and y.rect.centerx + -z.radius  < z.rect.centerx and y.rect.centery + z.radius  > z.rect.centery and y.rect.centery + -z.radius  < z.rect.centery:
                                    if z.cooldown <= 0:
                                        if type(z) is t2 :
                                                bl_ = projectile(1000, 1000,z.rect.centerx,z.rect.centery)
                                                bl_.image = bdf
                                                bl_.target = type(y)
                                                placed.add(bl_)
                                                bl_.place = 1
                                        elif type(z) is t1 :
                                                bl_ = projectile(1000, 1000,z.rect.centerx,z.rect.centery)
                                                bl_.target = type(y)
                                                placed.add(bl_)
                                                bl_.place = 1
                                        if z.taken == 0:
                                            y.health = y.health - z.degat
                                        if z.takenbase != 0:
                                            z.taken = 1
                                        z.cooldown = z.cooldownorigin
                                            
                                    else :
                                        z.cooldown = z.cooldown - 1
                                    if z.rect.centerx - 90 < y.rect.centerx:
                                        y.avancev = 0
                                    if z.rect.centery + 50 < y.rect.centery and z.rect.centery - 50 > y.rect.centery :
                                        y.movtower = 0
                                    elif z.rect.centery  > y.rect.centery :
                                        y.movtower = 15
                                    elif z.rect.centery - 75 < y.rect.centery :
                                        y.movtower = -15
                                    if y.health <= 0:
                                        pygame.sprite.Group.remove(placed, y)
                                    
        
        for z in placed:
            if type(z) is enemi1 or type(z) is enemi2 or type(z) is enemi3:
                for y in placed:
                    if type(y) is t1 or type(y) is t2 or type(y) is mur:
                        if y.rect.centerx + z.radius > z.rect.centerx and y.rect.centerx + -z.radius < z.rect.centerx and y.rect.centery + z.radius > z.rect.centery and y.rect.centery + -z.radius < z.rect.centery:
                            y.health = y.health - z.degat
                            if y.health <= 0 :
                                pygame.sprite.Group.remove(placed, y)
        
        # Boucle déplacement des enemis
    
        for i in placed:
            if type(i) is enemi1 or type(i) is enemi2 or type(i) is enemi3:
                if i.rect.centerx > round(ecran.get_width() * 0.89 , 100):
                    vie_mur = vie_mur -1
                    pygame.sprite.Group.remove(placed, i)
                i.avance()
                i.avancev = 50
                i.movtower = 0
                print(i) 
        
        for z in placed:
            if type(z) is t1 or type(z) is t2:
                z.taken = 0
        
        if vie_mur <= 0:
            with open("ecran attacker won.py") as f:
                exec(f.read())
        
    for p in placed:
        if type(p) is projectile:
            for y in placed:
                if type(y) is p.target:
                    if p.rect.centerx == y.rect.centerx :
                        p.speed = 0
                    if p.rect.centery > y.rect.centery + 10:
                        p.angle = -10
                    elif p.rect.centery > y.rect.centery - 10:
                        p.angle = 10
                    else :
                        p.angle = 0
                    if y.rect.centerx + 2 > p.rect.centerx and y.rect.centerx + -2 < p.rect.centerx and y.rect.centery + 5 > p.rect.centery and y.rect.centery + -5 < p.rect.centery:
                        pygame.sprite.Group.remove(placed, p) 
                    if p.rect.centerx < y.rect.centerx :
                        pygame.sprite.Group.remove(placed, p)

            p.avance()
                        
    # Entrée des input côté joueur
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
            
            if event.key == pygame.K_a:
                pygame.sprite.Group.empty(souris)
                if joueur == 1:
                    selectione = 2
                    souris.add(sr_)
                    rad = sr_.radius
                    textstats = font.render(str(sr_.health) + " vie / " + str(sr_.degat) + " dégat / " + str(sr_.cost) + " coût", True, (10, 10, 10))
                if joueur == 2:
                    selectione = 2
                    souris.add(enemi1_)
                    rad = enemi1_.radius
                    textstats = font.render(str(enemi1_.health) + " vie / " + str(enemi1_.degat) + " dégat / " + str(enemi1_.cost) + " coût", True, (10, 10, 10))
                
            if event.key == pygame.K_e:
                pygame.sprite.Group.empty(souris)
                if joueur == 1:
                    selectione = 3
                    souris.add(sr2_)
                    rad = sr2_.radius
                    textstats = font.render(str(sr2_.health) + " vie / " + str(sr2_.degat) + " dégat / " + str(sr2_.cost) + " coût", True, (10, 10, 10))
                if joueur == 2:
                    selectione = 3
                    souris.add(enemi2_)
                    rad = enemi2_.radius
                    textstats = font.render(str(enemi2_.health) + " vie / " + str(enemi2_.degat) + " dégat / " + str(enemi2_.cost) + " coût", True, (10, 10, 10))
            
            if event.key == pygame.K_q:
                pygame.sprite.Group.empty(souris)
                if joueur == 1:
                    selectione = 4
                    souris.add(sr3_)
                    rad = sr3_.radius
                    textstats = font.render(str(sr3_.health) + " vie / " + str(sr3_.degat) + " dégat / " + str(sr3_.cost) + " coût", True, (10, 10, 10))
                if joueur == 2:
                    selectione = 4
                    souris.add(enemi3_)
                    rad = enemi3_.radius
                    textstats = font.render(str(enemi3_.health) + " vie / " + str(enemi3_.degat) + " dégat / " + str(enemi3_.cost) + " coût", True, (10, 10, 10))
                
            if event.key == pygame.K_z:
                selectione = 1
                pygame.sprite.Group.empty(souris)
                textstats = font.render("", True, (10, 10, 10))
                
        #Entrée input souis avec condition :
        #tour sééectionée->vérif partie écran->argent->entrée position sprites
        
        if pygame.mouse.get_pressed()[0]:
            if selectione == 2:
                if pygame.mouse.get_pos() > (ecran.get_width() / 2 , 100) and joueur == 1 and pygame.mouse.get_pos() < (ecran.get_width() * 0.90 , 100):
                    if money >= 100:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            tower_ = t1(1000, 1000,cox,coy) 
                            placed.add(tower_)
                            money = money - tower_.cost
                elif joueur == 2 and pygame.mouse.get_pos() < (ecran.get_width() / 2 , 100):
                    if money >= 100:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            object_ = enemi1(1000, 1000,cox,coy )
                            placed.add(object_)
                            money = money - object_.cost
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
                    
            if selectione == 3:
                if pygame.mouse.get_pos() > (ecran.get_width() / 2 , 100) and joueur == 1 and pygame.mouse.get_pos() < (ecran.get_width() * 0.90 , 100):
                    if money >= 100:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            tower_ = t2(1000, 1000,cox,coy) 
                            placed.add(tower_)
                            money = money - tower_.cost
                elif joueur == 2 and pygame.mouse.get_pos() < (ecran.get_width() / 2 , 100):
                    if money >= 100:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            object_ = enemi2(1000, 1000,cox,coy )
                            placed.add(object_)
                            money = money - object_.cost
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
                    
            if selectione == 4:
                if pygame.mouse.get_pos() > (ecran.get_width() / 2 , 100) and joueur == 1 and pygame.mouse.get_pos() < (ecran.get_width() * 0.90 , 100):
                    if money >= 50:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            tower_ = mur(1000, 1000,cox,coy) 
                            placed.add(tower_)
                            money = money - tower_.cost
                            print(tower_.rect.center)
                elif joueur == 2 and pygame.mouse.get_pos() < (ecran.get_width() / 2 , 100):
                    if money >= 100:
                        if sprtls[len(sprtls) - 1] != pygame.mouse.get_pos():
                            sprtls.append((pygame.mouse.get_pos()))
                            cox,coy = sprtls[len(sprtls) - 1]
                            object_ = enemi3(1000, 1000,cox,coy )
                            placed.add(object_)
                            money = money - object_.cost
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
    
    
    #activation écran / update
    clock.tick(60)
    ecran.blit(nouvelle_image,(0,0))
    souris.update()
    placed.update() 
    if selectione != 1 :
        pygame.draw.circle(ecran, black, pygame.mouse.get_pos(),rad, 5)
    textargent = font.render(str(money)+"$", True, (10, 10, 10))
    ecran.blit(textjoueur, textposjoueur)
    ecran.blit(texttemps, textpostemps)
    ecran.blit(textargent, textposargent)
    ecran.blit(textstats, textposstats)
    souris.draw(ecran)
    placed.draw(ecran) 
    pygame.display.update() 
    

pygame.quit()
