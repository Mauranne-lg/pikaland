from player import Player
from goat import Goat
import pygame



# creer une classe player
class Game:

    def __init__(self):
        # On génère notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de goat
        self.all_goats = pygame.sprite.Group()
        # Permet un déplacement fluide du player
        self.pressed = {}
        self.spawn_goat()

    def spawn_goat(self):
        goat = Goat(self)
        self.all_goats.add(goat)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
