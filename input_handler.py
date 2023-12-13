import pygame

class InputHandler:
    @staticmethod
    def get_keys():
        return pygame.key.get_pressed()