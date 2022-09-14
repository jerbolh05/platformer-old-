import pygame
import random
from settings import *
from entities import *

class Platform(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Goal(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.animation_speed = 5

    def update(self):
        self.animate()
        
class WalkThru(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Ladder1(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

    def apply(self, player):
        player.rect.y -= 2

class Ladder2(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

    def apply(self, player):
        player.rect.y += 2

class Message(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
    
