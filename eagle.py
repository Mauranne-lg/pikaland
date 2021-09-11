import pygame
import random


class Eagle(pygame.sprite.Sprite):

    def __init__(self, eagle_event):
        super().__init__()
        # def l'image associée
        self.image = pygame.image.load('assets/eagle.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 8)
        self.rect.x = random.randint(20, 1100)
        self.rect.y = - random.randint(0, 800)
        self.eagle_event = eagle_event

    def remove(self):
        self.eagle_event.all_eagles.remove(self)

        # verifier si nb d'aigles a zero
        if len(self.eagle_event.all_eagles) == 0:
            # on remet la jauge à zero
            self.eagle_event.reset_percent()
            # faire reapparaitre les chevres
            self.eagle_event.game.spawn_goat()

    def fall(self):
        self.rect.y += self.velocity

        # disparait quand sol touché
        if self.rect.y >= 500:
            self.remove()
        # si boule de feu touche le joueur
        if self.eagle_event.game.check_collision(self, self.eagle_event.game.all_players):
            # on retire la boule de feu
            self.remove()

            # s'il n'y a plus de boule de feu
            if len(self.eagle_event.all_eagles) == 0:
                # remettre jauge au début
                self.eagle_event.reset_percent()
                self.eagle_event.fall_mode = False

            # on enleve 20 points de vie au joueur
            self.eagle_event.game.player.damage(20)
