import pygame, sys
from pygame import locals as loc

#starting pygame
pygame.init()

#parameters of display
HEIGHT = 600
WIDTH = 800

#colors
SPACE_COLOR = 14, 21, 58
WHITE = 226, 243, 245

#FPS
FPS = 60
FrameControl = pygame.time.Clock()

#creating window
display = pygame.display.set_mode((WIDTH, HEIGHT))
#filling window with colors
display.fill(SPACE_COLOR)

#title of window
pygame.display.set_caption("Aliens")

#enemy
class Alien(pygame.sprite.Sprite):
    def __init__(self, sX, sY, speed):
        super().__init__()
        #picture of enemy
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = WIDTH / 2
        #speed of enemy
        self.speed = speed
        self.vX = self.speed
        self.vY = sY
        self.drop = 0
        self.velocity = {'x': self.vX , 'y': self.vY}

#drawing an window with enemies
    def draw(self, surface): 
        surface.blit(self.image, self.rect)

#redrowing to make all objects move
    def update(self):
        #moving
        if self.rect.right > WIDTH or self.rect.left < 0:
            if self.drop <= 40:
                self.drop += 1
                self.speed = -self.speed
                self.vX = 0
                self.vY = 2
            elif self.drop > 40:
                self.vY = 0
                self.vX = self.speed
                self.drop = 0
        if self.rect.bottom > HEIGHT:
            self.reset()
            
        self.velocity = {'x': self.vX , 'y': self.vY}

#turning enemies to their start position
    def reset(self):
        self.rect.top = 0
        self.rect.left = WIDTH / 2
        self.vX = self.speed
        self.vY = 0
        self.drop = 0
        self.velocity = {'x': self.vX , 'y': self.vY}

#true moving of enemies
    def move(self):
        self.rect.move_ip(self.velocity['x'], self.velocity['y'])

#enemes in objects
alien1 = Alien(2, 0, 2)
alien2 = Alien(3, 0, 3)
alien3 = Alien(5, 0, 4)
aliens = [alien1, alien2, alien3]
#game
while True:
    for e in pygame.event.get():
        if e.type == loc.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(SPACE_COLOR)

    # game engine
    for alien in aliens:
        alien.update()

        alien.draw(display)
        alien.move()
    # end game engine

    pygame.display.update()
    FrameControl.tick(FPS)