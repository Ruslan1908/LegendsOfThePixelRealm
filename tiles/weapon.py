import pygame
from audio import play_sound


class Sword(pygame.sprite.Sprite):
    def __init__(self, player, duration=200):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/weapon/sword.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.duration = duration  # czas życia miecza (ms)
        self.start_time = pygame.time.get_ticks()
        self.player = player
        self.set_position()

    def set_position(self):
        """Ustawia pozycję miecza względem gracza."""
        self.rect.midleft = self.player.rect.midright

    def update(self):
        """Usuwa miecz po upływie określonego czasu."""
        if pygame.time.get_ticks() - self.start_time > self.duration:
            self.kill()