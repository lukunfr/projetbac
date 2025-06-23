import pygame
import random

# Initialisation de Pygame et de la fenêtre
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

# Chargement des images
background = pygame.transform.scale(pygame.image.load('background.jpg'), (1200, 600))
book_img = pygame.transform.scale(pygame.image.load('book.png'), (60, 60))

# Variables du livre (joueur)
book_x = 100
book_y = 300
y_velocity = 0
gravity = 0.5
jump_force = -10

# Variables de l'obstacle (tuyau)
obstacle_x = 1200
obstacle_width = 60
gap_height = 210
gap_y = random.randint(80, 340)
obstacle_speed = 4

background_x = 0
started = False

while True:
    # Réinitialisation à chaque partie
    book_y = 300
    y_velocity = 0
    obstacle_x = 1200
    gap_y = random.randint(80, 340)
    started = False
    background_x = 0
    running = True

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                started = True
                y_velocity = jump_force

        # Défilement du fond
        background_x -= 2
        if background_x <= -1200:
            background_x = 0
        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + 1200, 0))

        if started:
            # Gravité et déplacement du livre
            y_velocity += gravity
            book_y += y_velocity
            if book_y >= 540:
                book_y = 540
                y_velocity = 0
            if book_y <= 0:
                book_y = 0
                y_velocity = 1

            # Déplacement de l'obstacle
            obstacle_x -= obstacle_speed
            if obstacle_x + obstacle_width < 0:
                obstacle_x = 1200
                gap_y = random.randint(80, 340)

            # Dessin de l'obstacle (haut et bas)
            pygame.draw.rect(screen, (200, 50, 50), (obstacle_x, 0, obstacle_width, gap_y))
            bottom_y = gap_y + gap_height
            pygame.draw.rect(screen, (200, 50, 50), (obstacle_x, bottom_y, obstacle_width, 600 - bottom_y))

            # Collision
            book_rect = pygame.Rect(book_x, book_y, 60, 60)
            top_rect = pygame.Rect(obstacle_x, 0, obstacle_width, gap_y)
            bottom_rect = pygame.Rect(obstacle_x, bottom_y, obstacle_width, 600 - bottom_y)
            if book_rect.colliderect(top_rect) or book_rect.colliderect(bottom_rect):
                running = False

        # Affichage du livre
        screen.blit(book_img, (book_x, book_y))
        pygame.display.flip()

    # Message de fin et attente d'un clic pour recommencer
    text = font.render("HAHA fallais mieux réviser", True, (255, 255, 255))
    rect = text.get_rect(center=(600, 300))
    screen.blit(text, rect)
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                wait = False