import pygame
from eagle import Eagle


# creation class pour
class EagleFallEvent:

    # lors du chargement, on crée un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker nos eagles
        self.all_eagles = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def eagle_fall(self):
        self.game.sound_manager.play('eagles')
        # boucle pour faire apparaitre 1 et 10 aigles
        for i in range(1, 20):
            # on fait apparaitre un aigle
            self.all_eagles.add(Eagle(self))

    def attempt_fall(self):
        # si la jauge est chargée
        if self.is_full_loaded() and len(self.game.all_goats) == 0:
            self.eagle_fall()
            self.fall_mode = True # activer l'evenement

    def update_bar(self, surface):

        # on incremente la barre
        self.add_percent()

        # barre noir en bg
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            surface.get_width(),  # longueur de la fenetre
            10  # epaisseur barre
        ])
        # barre rouge
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur barre
        ])
