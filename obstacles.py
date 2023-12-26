from random import randint
import pygame
obstacles = []
scuffed_timer = 0

def create_rect():
    global scuffed_timer
    scuffed_timer += 1
    if scuffed_timer == 20:
        scuffed_timer = 0

        if randint(1,2) == 1:
            list = [0,2,3]
        else:
            list = [1]
        for i in list:
            obstacles.append(Obstacles(pygame.Rect(1300,i*100,100,100)))
    

class Obstacles:
    def __init__(self, rect):
        self.rect = rect
    def movement(self):
        self.rect.x -= 5
    def draw(self, screen):
        pygame.draw.rect(screen,("#480a23"),self.rect)
    def update(self, screen):
        self.movement()
        self.draw(screen)
    