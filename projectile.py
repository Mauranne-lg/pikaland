import pygame


# creer une classe player
class Projectile(pygame.sprite.Sprite):

    #constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/daisy.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le proj
        self.angle += -6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # si notre projectile n'est plus visible
        if self.rect.x > 1280:
            # suppr le proj
            self.remove()