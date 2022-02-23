import pygame, sys
from pygame import locals as loc

pygame.init()

HEIGHT = 600
WIDTH = 800

SPACE_COLOR = 14, 21, 58
WHITE = 226, 243, 245

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(SPACE_COLOR)

pygame.display.set_caption("Aliens")


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.top = HEIGHT / 2
        self.rect.left = WIDTH / 2
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)


alien = Alien()

while True:
    for e in pygame.event.get():
        if e.type == loc.QUIT:
            pygame.quit()
            sys.exit()

    # game engine
    alien.draw(display)
    # end game engine

    pygame.display.update()
