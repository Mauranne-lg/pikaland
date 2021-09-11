from player import Player
from goat import Goat
from eagle_event import EagleFallEvent
import pygame


# creer une classe player
class Game:

    def __init__(self):
        # on définit si notre jeu a commencé ou non
        self.is_playing = False
        # On génère notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evt
        self.eagle_event = EagleFallEvent(self)
        # groupe de goat
        self.all_goats = pygame.sprite.Group()

        # Permet un déplacement fluide du player
        self.pressed = {}
        self.spawn_goat()
        self.spawn_goat()

    def game_over(self):
        # remettre le jeu à zéro (pas de monstre, jeu en attente, vie du joeur à 0)
        self.all_goats = pygame.sprite.Group()
        self.eagle_event.all_eagles = pygame.sprite.Group()
        self.eagle_event.reset_percent()
        self.player.health = 100
        self.is_playing = False

    def update(self, screen):
        # appliquer image joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser barre vie joueur
        self.player.update_health_bar(screen)

        # actualiser barre du jeu
        self.eagle_event.update_bar(screen)

        # recuperer les proj du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les goats du joueur
        for goat in self.all_goats:
            goat.forward()
            goat.update_health_bar(screen)

        # recuperer les eagles de notre jeu
        for eagle in self.eagle_event.all_eagles:
            eagle.fall()

        # on applique l'ensemble des images
        self.player.all_projectiles.draw(screen)

        # on applique l'ensemble des images du groupe de chèvres
        self.all_goats.draw(screen)

        # appliquer le groupe d'aigles
        self.eagle_event.all_eagles.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_goat(self):
        goat = Goat(self)
        self.all_goats.add(goat)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
