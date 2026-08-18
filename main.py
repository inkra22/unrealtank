import pygame
import time
import math
from  bulletsnwpns import *
from utility import *

pygame.init()
clock = pygame.time.Clock()
FPS = 128
RADIUS = 10
SPEED = 1
TLENGTH = 30
TWIDTH = 5
BULSPEED = 5

resx=1500
resy=700
screen = pygame.display.set_mode((resx,resy))

class Weapon:
    def __init__(self, given_name):
        self.name = given_name


class Player:
    def __init__(self, given_name, colour, x, y):
        self.name: str = given_name
        self.x: int = x
        self.y:int = y
        self.weapons: list[Weapon] = []
        self.colour = colour
        self.angle = 0
        self.tendx = 0 
        self.tendy = 0
        self.last_fired = 0
        self.ammo = 100
        self.hp = 100

    def walk(self,FoB):
        Udx = SPEED*math.cos(self.angle)
        Udy = SPEED*math.sin(self.angle)
        self.x = self.x + FoB*Udx
        self.y = self.y + FoB*Udy
        if self.x < RADIUS:
            self.x = RADIUS
        if self.x > resx-RADIUS:
            self.x = resx-RADIUS
        if self.y < RADIUS:
            self.y = RADIUS
        if self.y > resy-RADIUS:
            self.y = resy-RADIUS 

    #def strafeold(self, LoR):
        #Ldir = SPEED*math.cos(self.angle - 90*math.pi/180)
        #Rdir = SPEED*math.sin(self.angle + 90*math.pi/180)
        #self.x = self.x + LoR*Ldir
        #self.y = self.y + LoR*Rdir

    def strafe(self, LoR):
        strafex = SPEED*math.cos(self.angle - (LoR*90)*math.pi/180)
        strafey = SPEED*math.sin(self.angle - (LoR*90)*math.pi/180)
        self.x = self.x + strafex
        self.y = self.y + strafey

    def rotate(self, deltaAngle):
        self.angle = self.angle + deltaAngle

    def pickWeapon(self, w: Weapon):
        self.weapons.append(w)

    def shoot(self):
        if self.ammo <= 0:
            return None
        
        current_time = time.time()
        if(current_time - self.last_fired < 0.5):
            return None
        
        b = Sniper(self.tendx, self.tendy, self.angle, self.colour)
        self.last_fired = time.time()
        self.ammo -= 1
        return b
    
    def take_hit(self, b: Bullet):
        self.hp -= b.dmg
        Udx = 20 * math.cos(b.angle)
        Udy = 20 * math.sin(b.angle)
        self.x += Udx
        self.y += Udy
        if self.hp < 0:
            self.hp = 0



    def render(self):
        pygame.draw.circle(screen,self.colour, (self.x,self.y), RADIUS)
        Tdx=TLENGTH*math.cos(self.angle)
        Tdy=TLENGTH*math.sin(self.angle)
        self.tendx = self.x+Tdx
        self.tendy = self.y+Tdy
        pygame.draw.line(screen,self.colour, (self.x,self.y),(self.x+Tdx,self.y+Tdy),TWIDTH)



p1 = Player("Zaain", "red", 50, 50)
p2 = Player("Mumthaz", "blue", 1450, 650)

liveammo: list[Bullet] = []


def updateHUD():
#p1
    
    font = pygame.font.SysFont("Arial", 15)
    surface = font.render(p1.name, 1, "white")
    screen.blit(surface, (10,10))

    surface = font.render("ammo:" + str(p1.ammo), 1, "white")
    screen.blit(surface, (10,25))

    surface = font.render("health:" + str(p1.hp), 1, "white")
    screen.blit(surface, (10,40))

#p2

    surface = font.render(p2.name, 1, "white")
    screen.blit(surface, (1400,10))
    
    surface = font.render("ammo:" + str(p2.ammo), 1, "white")
    screen.blit(surface, (1400,25))

    surface = font.render("health:" + str(p2.hp), 1, "white")
    screen.blit(surface, (1400,40))


Runn=True
while Runn:
    events=pygame.event.get()

    for e in events:
        if e.type == 256:
            Runn = False

    keys = pygame.key.get_pressed()
#p1
    
    if keys[pygame.K_a]:
        p1.rotate(-3.14/180*1)
    if keys[pygame.K_d]:
        p1.rotate(3.14/180*1)
    if keys[pygame.K_w]:
        p1.walk(1)
    if keys[pygame.K_s]:
        p1.walk(-1)
    if keys[pygame.K_e]:
        p1.strafe(-1)
    if keys[pygame.K_q]:
        p1.strafe(1)
    if keys[pygame.K_LSHIFT]:
        newbul = p1.shoot()
        if newbul != None:
            liveammo.append(newbul)

# p2
        
    if keys[pygame.K_j]:
        p2.rotate(-3.14/180*1)
    if keys[pygame.K_l]:
        p2.rotate(3.14/180*1)
    if keys[pygame.K_i]:
        p2.walk(1)
    if keys[pygame.K_k]:
        p2.walk(-1)
    if keys[pygame.K_o]:
        p2.strafe(-1)
    if keys[pygame.K_u]:
        p2.strafe(1)
    if keys[pygame.K_b]:
        newbul = p2.shoot()
        if newbul != None:
            liveammo.append(newbul)



    screen.fill("black")
    p1.render()        
    p2.render()
   
    for bullet in liveammo:
        bullet.update()
        if bullet.alive == False:
            liveammo.remove(bullet)
        
        else:
            if circ_hitreg((p1.x, p1.y, RADIUS), (bullet.x, bullet.y, bullet.radius)):
                p1.take_hit(bullet)
                liveammo.remove(bullet)

            if circ_hitreg((p2.x, p2.y, RADIUS), (bullet.x, bullet.y, bullet.radius)):
                p2.take_hit(bullet)
                liveammo.remove(bullet)

        bullet.render(screen)
    
    updateHUD()
    pygame.display.flip()
    clock.tick(FPS)