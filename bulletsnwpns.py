import pygame
import math



class Bullet:
    def __init__(self,x ,y ,angle, colour):
        self.x: int = x
        self.y: int = y
        self.angle: float = angle
        self.speed: int = 5
        self.mxdist: int = 1000
        self.colour: str = colour
        self.dmg: int = 5
        self.distravel = 0
        self.alive = True
        self.radius = 10

    def update(self):
        self.x = self.x + self.speed * math.cos(self.angle)
        self.y = self.y + self.speed * math.sin(self.angle)
        self.distravel += self.speed
        if self.distravel == self.mxdist:
            self.alive = False



    def render(self, surface):
        if self.alive:
            pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)

class Sniper(Bullet):
    def __init__(self, x, y, angle, colour):
        super().__init__(x, y, angle, colour)
        self.speed: int = 25
        self.mxdist = 3000
        self.radius = 10
        #dammage curve asc /w range
        
