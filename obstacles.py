from random import randint
import pygame
obstacles = []

def create_rect():
    if randint(1,2):
        obstacles.append(Obstacles(pygame.Rect(1300,200,50,50)))
    

class Obstacles:
    def __init__(self, rect):
        self.rect = rect
    def movement(self):
        self.rect.x -= 5
    def draw(self):
        global screen
        pygame.draw.rect(screen,("#480a23"),self.rect)
        print("a")
    def update(self):
        self.movement()
        self.draw()
    