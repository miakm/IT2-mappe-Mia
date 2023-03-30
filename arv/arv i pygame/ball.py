import pygame
pygame.init()
clock = pygame.time.Clock()


width = 320
height = 240
speedX = 2
speedY = 2
black = (0, 0, 0)
running = True

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballrect = ballrect.move((speedX,speedY))
    if ballrect.left < 0 or ballrect.right > width:
        speedX = -speedX
    if ballrect.top < 0 or ballrect.bottom > height:
        speedY = -speedY

    screen.fill(black)
    screen.blit(ball, ballrect)
    

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()