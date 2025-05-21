import pygame


class QuestPanel:
    def __init__(self, quest_manager, screen):
        self.quest_manager = quest_manager
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.width = 300
        self.height = 400
        self.bg_color = (30, 30, 30)
        self.border_color = (255, 255, 255)
        self.active = False  # Panel domyślnie ukryty

    def toggle(self):
        """Przełącza widoczność panelu z zadaniami."""
        self.active = not self.active

    def draw(self):
        """Rysuje panel z aktualnymi zadaniami."""
        if not self.active:
            return
        panel_rect = pygame.Rect(50, 50, self.width, self.height)
        pygame.draw.rect(self.screen, self.bg_color, panel_rect)
        pygame.draw.rect(self.screen, self.border_color, panel_rect, 2)

        y_offset = 60
        for quest in self.quest_manager.quests:
            quest_text = f"{quest.description} [{quest.progress}/{quest.target}]"
            if quest.completed:
                quest_text += " (Wykonane)"
            text_surface = self.font.render(quest_text, True, (255, 255, 0))
            self.screen.blit(text_surface, (60, y_offset))
            y_offset += 30