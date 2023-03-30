

# Example file showing a basic pygame "game loop"
import pygame
from random import randint
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

biden = pygame.image.load("joe.png")
iskrem = pygame.image.load("ice.png")


class Figur:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def tegn(self):
        screen.blit(biden, (self._x,self._y))

class Spiller(Figur):
    def __init__(self, x, y, fartY):
        super().__init__(x, y)
        self._fartY = fartY
    
    def hopp(self):
        self._y -= 10
        self._x -= 4

    def fall(self):
        self._y += 4
        self._x += 2

    def er_over_hinder(self):
        pass

class Hinder(Figur):
    def __init__(self, x, y, fartX, hoyde, bredde):
        super().__init__(x, y)
        self._fartX = fartX
        self._hoyde = hoyde
        self._bredde = bredde
    
    def tegn(self, screen):
        screen.blit(iskrem, (self._x,self._y))

    def flytt_venstre(self):
        self._x += 1

sirkel = Figur(30,100)
spiller = Spiller(100,50,50)
hindere = [] 
for i in range(8): 
    height = randint(20,100)
    a = randint(10,100)
    b = randint(10,200)
    nytt_hinder = Hinder(a, b, 100, height, 10) 
    hindere.append(nytt_hinder) 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # LAG SPILLET DIT HER:

    spiller.tegn()

    for hinder in hindere:
        hinder.flytt_venstre() 
        hinder.tegn(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        spiller.hopp()
    spiller.fall()
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()