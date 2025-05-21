import random
import pygame
from enemy.skeleton import Skeleton
from enemy.goblin import Goblin
from enemy.werewolf import Werewolf

class EnemyManager:
    def __init__(self, dungeon_map, player):
        """
        Inicjalizuje menedżera przeciwników.
        dungeon_map: obiekt mapy poziomu,
        player: obiekt gracza (do określenia pozycji).
        """
        self.enemies = pygame.sprite.Group