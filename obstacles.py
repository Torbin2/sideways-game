from random import randint
import pygame
obstacles = []
scuffed_timer = 0

def create_rect():
    global scuffed_timer
    scuffed_timer += 1
    if scuffed_timer == 50:
        scuffed_timer = 0

        x = randint(1,3)
        if x == 1:
            list = [0,2,3]
        elif x == 2:
            list = [1,2]
        elif x== 3:
            list = [0,1,3]
        elif x==4:
            list = [0,3]
        for i in list:
            obstacles.append(Obstacles(pygame.Rect(1300,i*100,100,100)))
    

class Obstacles:
    def __init__(self, rect):
        self.rect = rect
        self.stopped = False
    def movement(self):
        if not self.stopped:
            self.rect.x -= 5
    def draw(self, screen):
        pygame.draw.rect(screen,("#480a23"),self.rect)
    def collision(self):
        #screen
        if self.rect.left <= 0 and not self.stopped:
            self.rect.left = 0
            self.stopped = True
        for i in obstacles:
            if self.rect.colliderect(i) and i != self:
                i.left = self.rect.right
                i.stopped = True
    
    def remove(self):
        if self.stopped:
            if self.rect.x <= -100:
                print(self.rect.x)
                return True
                
    
    def update(self, screen):
        self.movement()
        self.draw(screen)
        self.collision()
    