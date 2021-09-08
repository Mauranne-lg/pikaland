import pygame
from projectile import Projectile


# creer une classe player
class Goat(pygame.sprite.Sprite):

    #constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 2
        self.image = pygame.image.load('assets/goat.png')
        self.image = pygame.transform.scale(self.image, (300, 180))
        self.rect = self.image.get_rect()
        self.rect.x = 1150
        self.rect.y = 400

    def forward(self):
        # si pas de collision avec groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


