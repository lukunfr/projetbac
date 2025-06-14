import pygame

pygame.init()

    # Set-up de tout le graphique
screen = pygame.display.set_mode((1200, 600))
screen_width, screen_height = screen.get_size()
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))
book = pygame.image.load("book.png")
book = pygame.transform.scale(book, (60, 60))
crayon = pygame.image.load("crayon.png")
crayon = pygame.transform.scale(crayon, (200, 410))
gomme = pygame.image.load("gomme.png")


running = True

x, y = 100, 300 # position définit pour tout object si ce n'est pas précisé.
velocity = 1 # Rapidité
gravity = 0.005   #Gravité de l'objet
jump = -1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Action de la souris en cliquant gauche
            velocity = jump #Mise en place du "saut".


    # Définir le placement/déplacements/saut
    velocity += gravity
    velocity = max(min(velocity, 5), -2)
    y += velocity
    if y > 550:
        y = 550
        velocity = 0



    # BACKGROUND
    screen.fill((0, 0, 0))  # Rafraichissement de l'écra
    screen.blit(background, (0,0)) #Affiche le fond d'écran
    screen.blit(book, (x,y))    # en deuxieme l'oisea
    screen.blit(crayon, (300, 270))
    pygame.display.flip()  # L'affichage pour mettre les "objects" à l'écran

pygame.quit()

# à faire :
# Graviter
# Images
