import pygame

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.x = 500
        self.y = 500


    def render(self, surface):
        pygame.draw.circle(surface, "red",  (self.x, self.y))