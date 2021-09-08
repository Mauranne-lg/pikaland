# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from game import Game

pygame.init()


# générer la fenetre du jeu
pygame.display.set_caption("Pika game")
screen = pygame.display.set_mode((1280, 620))

# importe l'image de bg du jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

running = True

# boucle du jeu, tant que vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, 0))

    # appliquer image joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les proj du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les goats du joueur
    for goat in game.all_goats:
        goat.forward()

    # on applique l'ensemble des images
    game.player.all_projectiles.draw(screen)

    # on applique l'ensemble des images du groupe de chèvres
    game.all_goats.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
            game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # si l'evt est la fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si joueur lache touche clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si touche espace enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
