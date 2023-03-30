# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_x = 50
player_y = 100

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", (player_x, player_y), 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()