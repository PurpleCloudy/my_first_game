import pygame, sys
from pygame import locals as loc

pygame.init()

HEIGHT = 600
WIDTH = 800

SPACE_COLOR = 14, 21, 58
WHITE = 226, 243, 245

FPS = 60
FrameControl = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(SPACE_COLOR)

pygame.display.set_caption("Aliens")


class Alien(pygame.sprite.Sprite):
    def __init__(self, sX, sY, speed):
        super().__init__()
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = WIDTH / 2
        self.speed = speed
        self.vX = self.speed
        self.vY = sY
        self.drop = 0
        self.velocity = {'x': self.vX , 'y': self.vY}

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
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

    def reset(self):
        self.rect.top = 0
        self.rect.left = WIDTH / 2
        self.vX = self.speed
        self.vY = 0
        self.drop = 0
        self.velocity = {'x': self.vX , 'y': self.vY}

    def move(self):
        self.rect.move_ip(self.velocity['x'], self.velocity['y'])

alien1 = Alien(2, 0, 2)
alien2 = Alien(3, 0, 3)
alien3 = Alien(5, 0, 4)
aliens = [alien1, alien2, alien3]
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