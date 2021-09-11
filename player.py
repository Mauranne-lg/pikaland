import pygame
from projectile import Projectile

# creer une classe player
class Player(pygame.sprite.Sprite):

    #constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.image = pygame.transform.flip(self.image, 180, 0)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 470

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessine la barre de vie (surface, couleur de la barre, position de la barre)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (0, 160, 193), [self.rect.x + 20, self.rect.y - 20, self.health, 7])

    def launch_projectile(self):
        # on crée une instance de Projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec une chèvre
        if not self.game.check_collision(self, self.game.all_goats):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

