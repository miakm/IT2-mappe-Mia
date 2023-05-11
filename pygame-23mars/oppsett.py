
import pygame
from random import randint
import time


pygame.init()
pygame.font.init()


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

biden = pygame.image.load("joe.png")
biden = pygame.transform.scale(biden, (160,120))
iskrem = pygame.image.load("ice.png")
iskrem = pygame.transform.scale(iskrem, (100, 100))


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
        if 0 <= self._y:
            self._y -= 10

    def side_h(self):
        if self._x < 1280-140:
            self._x += 10

    def side_v(self):
        if 0 <= self._x:
            self._x -= 10

    def fall(self):
        if 720 - 100 > self._y:
            self._y += 6




class Hinder(Figur):
    def __init__(self, x, y, fartX, bredde):
        super().__init__(x, y)
        self._fartX = fartX
        self._hoyde = randint(20, 600)
        self._bredde = bredde
        self._y = 720 - self._hoyde
    
    def tegn(self, screen):
        screen.blit(iskrem, (self._x,self._y, self._bredde, self._hoyde))

    def flytt_venstre(self):
        self._x -= 2

sirkel = Figur(30,100)
spiller = Spiller(100,50,50)
hindere = [] 
m = randint(1,12)
for i in range(m): 
    b = randint(10,200)
    nytt_hinder = Hinder(1270, b, 100, 10) 
    hindere.append(nytt_hinder) 



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # LAG SPILLET DIT HER:
    spiller.tegn()


    for hinder in hindere:
        hinder.flytt_venstre() 
        hinder.tegn(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        spiller.hopp()
    elif keys[pygame.K_LEFT]:
        spiller.side_v()
    elif keys[pygame.K_RIGHT]:
        spiller.side_h()
    spiller.fall()


    score = 0
    # if spiller._y <= nytt_hinder._y and spiller._x <= nytt_hinder._x:
    #     score -= 10
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    head_text = font.render(f'Flappybiden', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(head_text, (200, 10))


    pygame.display.flip()
    clock.tick(60) 

pygame.quit()