from .base import Enemy

class Goblin(Enemy):
    def __init__(self, pos):
        super().__init__(pos, "assets/sprites/enemies/goblin.png", health=30, speed=2.0)