# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import pygame
from game import Game

pygame.init()

# definir une clock

clock = pygame.time.Clock()
FPS = 80

# générer la fenetre du jeu
pygame.display.set_caption("Pika game")
screen = pygame.display.set_mode((1280, 620))

# importe l'image de bg du jeu
background = pygame.image.load('assets/bg.jpg')

# importer la banniere
banner = pygame.image.load('assets/banner.png')

# importer le bouton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (220, 80))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.5)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)

# charger le jeu
game = Game()

running = True

# boucle du jeu, tant que vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, 0))

    # veirifer si jeu a commencé ou non
    if game.is_playing:
        # déclencher instructions partie
        game.update(screen)
    else:
        # ajouter ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (400, 40))

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
                game.sound_manager.play('tir')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si souris collision avec bouton joueur
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.is_playing = True
                game.sound_manager.play('start')

    #fixer le nombre de FPS sur ma clock
    clock.tick(FPS)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
