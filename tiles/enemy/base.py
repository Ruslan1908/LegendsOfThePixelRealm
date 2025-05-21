import pygame
import math
from audio import play_sound


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_path, health, speed):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.health = health
        self.speed = speed
        self.state = "idle"  # Możliwe stany: idle, chase, attack, dead

    def take_damage(self, amount):
        """Zmniejsza zdrowie wroga. Jeśli zdrowie spadnie do 0, zmienia stan na 'dead'."""
        self.health -= amount
        if self.health > 0:
            play_sound("hurt")
        else:
            self.state = "dead"
            play_sound("door")

    def update(self, player_pos):
        """Aktualizuje stan przeciwnika na podstawie odległości od gracza."""
        if self.state == "dead":
            return
        distance = math.hypot(player_pos[0] - self.rect.centerx, player_pos[1] - self.rect.centery)
        if distance < 40:
            self.state = "attack"
        elif distance < 200:
            self.state = "chase"
        else:
            self.state = "idle"

        if self.state == "chase":
            self.move_towards(player_pos)

    def move_towards(self, target_pos):
        """Porusza przeciwnika w kierunku pozycji gracza."""
        dx = target_pos[0] - self.rect.centerx
        dy = target_pos[1] - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
            self.rect.centerx += dx * self.speed
            self.rect.centery += dy * self.speed