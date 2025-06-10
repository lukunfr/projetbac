import pygame
from pygame.transform import scale

pygame.init()

screen = pygame.display.set_mode((600,800))
running = True

x, y = 100, 300 # position définit pour tout object si ce n'est pas précisé.
velocity = 1    # Rapidité
gravity = 1     #Gravité de l'objet
jump = 1
dy = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dy += 3
            while dy > 0:
                dy -= 0.5
                print('hey')


    # Définir le placement/déplacements/saut

    screen.fill((0,0,0)) # Rafraichissement de l'écra
    bird = pygame.image.load("bird.png")
    bird = pygame.transform.scale(bird, (50, 50))
    screen.blit(bird, (50, 50))# Example du bird
    pygame.display.flip()  # L'affichage pour mettre les "objects" à l'écran

pygame.quit()

# à faire :
# Graviter
# Images
