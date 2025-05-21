from .base import Enemy

class Skeleton(Enemy):
    def __init__(self, pos):
        super().__init__(pos, "assets/sprites/enemies/skeleton.png", health=50, speed=1.5)