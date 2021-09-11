import pygame
import random

# creer une classe player
class Goat(pygame.sprite.Sprite):

    #constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/goat.png')
        self.image = pygame.transform.scale(self.image, (300, 180))
        self.rect = self.image.get_rect()
        self.rect.x = 1150 + random.randint(000, 500)
        self.rect.y = 400
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # vérifier si encore en vie
        if self.health <= 0:
            # réapparition comme nouveau monstre
            self.rect.x = 1150 + random.randint(200, 800)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            # si la barre d'event est chargée à son max
            if self.game.eagle_event.is_full_loaded():
                # retirer du jeu
                self.game.all_goats.remove(self)

            # appel de la méthode pour essayer de déclencher l'attaque d'aigles
            self.game.eagle_event.attempt_fall()


    def update_health_bar(self, surface):
        # dessine la barre de vie (surface, couleur de la barre, position de la barre)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (0, 160, 193), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        # si pas de collision avec groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
        # infliger des degats au joueur
            self.game.player.damage(self.attack)


