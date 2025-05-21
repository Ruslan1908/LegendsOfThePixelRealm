from .base import Enemy

class Werewolf(Enemy):
    def __init__(self, pos):
        super().__init__(pos, "assets/sprites/enemies/werewolf.png", health=80, speed=1.2)