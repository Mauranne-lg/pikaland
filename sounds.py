import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'start': pygame.mixer.Sound("assets/sounds/start_game.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'eagles': pygame.mixer.Sound("assets/sounds/eagle_fall.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
            'goat': pygame.mixer.Sound("assets/sounds/goat.ogg")}

    def play(self, name):
        self.sounds[name].play()