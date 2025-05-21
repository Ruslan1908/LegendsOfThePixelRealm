import pygame


class HUD:
    def __init__(self, player, inventory, screen):
        self.player = player
        self.inventory = inventory
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.message = ""
        self.message_time = 0
        self.message_duration = 2000  # czas wyświetlania komunikatu (ms)
        self.dialogue = ""
        self.dialogue_time = 0
        self.dialogue_duration = 3000  # czas wyświetlania dialogu (ms)
        # Definiujemy prostą mini mapę jako prostokąt
        self.minimap_rect = pygame.Rect(screen.get_width() - 210, 10, 200, 200)

    def set_message(self, message):
        """Ustawia tymczasowy komunikat na HUD."""
        self.message = message
        self.message_time = pygame.time.get_ticks()

    def set_dialogue(self, text):
        """Ustawia tekst dialogu do wyświetlenia."""
        self.dialogue = text
        self.dialogue_time = pygame.time.get_ticks()

    def draw(self):
        """Rysuje rozszerzony interfejs (HUD) na ekranie."""
        # Pasek zdrowia
        health_bar_width = 200
        health_ratio = self.player.health / 100
        current_health_width = health_bar_width * health_ratio
        pygame.draw.rect(self.screen, (255, 0, 0), (20, 20, current_health_width, 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, health_bar_width, 20), 2)

        # Pasek many
        mana_bar_width = 200
        mana_ratio = self.player.mana / self.player.max_mana if self.player.max_mana > 0 else 1
        current_mana_width = mana_bar_width * mana_ratio
        pygame.draw.rect(self.screen, (0, 255, 255), (20, 50, current_mana_width, 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 50, mana_bar_width, 20), 2)

        # Pasek doświadczenia
        xp_bar_width = 200
        xp_ratio = self.player.experience / 100 if hasattr(self.player, "experience") else 0
        current_xp_width = xp_bar_width * xp_ratio
        pygame.draw.rect(self.screen, (0, 0, 255), (20, 80, current_xp_width, 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 80, xp_bar_width, 20), 2)

        # Ekwipunek
        x = 20
        y = 110
        for item in self.inventory.items:
            item_text = self.font.render(str(item), True, (255, 255, 255))
            self.screen.blit(item_text, (x, y))
            x += 100

        # Komunikat tymczasowy
        if self.message:
            current_time = pygame.time.get_ticks()
            if current_time - self.message_time < self.message_duration:
                message_surface = self.font.render(self.message, True, (255, 255, 0))
                rect = message_surface.get_rect(center=(self.screen.get_width() / 2, 20))
                self.screen.blit(message_surface, rect)
            else:
                self.message = ""

        # Dialog
        if self.dialogue:
            if pygame.time.get_ticks() - self.dialogue_time < self.dialogue_duration:
                dialogue_surface = self.font.render(self.dialogue, True, (255, 255, 255))
                dialogue_rect = dialogue_surface.get_rect(
                    center=(self.screen.get_width() / 2, self.screen.get_height() - 50))
                pygame.draw.rect(self.screen, (0, 0, 0), dialogue_rect.inflate(20, 20))
                self.screen.blit(dialogue_surface, dialogue_rect)
            else:
                self.dialogue = ""

        # Mini mapa
        pygame.draw.rect(self.screen, (50, 50, 50), self.minimap_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.minimap_rect, 2)