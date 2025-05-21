import pygame
from weapon import Sword
from audio import play_sound


class Player(pygame.sprite.Sprite):
    def __init__(self, knight_type):
        super().__init__()
        self.knight_type = knight_type
        self.sprites = []
        self.load_sprites()
        self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        self.rect = self.image.get_rect(center=(400, 300))
        self.health = 100
        self.mana = 80
        self.max_mana = 80
        self.experience = 0
        self.attack_cooldown = 500  # odstep pomiędzy atakami (ms)
        self.last_attack_time = 0

    def load_sprites(self):
        """Ładowanie animacji postaci."""
        for i in range(1, 3):
            sprite_path = f"assets/sprites/{self.knight_type}/{self.knight_type}_spritelist_{i}.png"
            sprite = pygame.image.load(sprite_path).convert_alpha()
            self.sprites.append(sprite)

    def update(self):
        """Aktualizacja animacji postaci."""
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def attack(self, weapon_group):
        """Metoda wykonująca atak – tworzy obiekt miecza."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            self.last_attack_time = current_time
            play_sound("attack")
            sword = Sword(self)
            weapon_group.add(sword)

    def take_damage(self, amount):
        """Zmniejszenie zdrowia gracza."""
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        """Procedura śmierci gracza."""
        print("Gracz zginął!")
        play_sound("hurt")