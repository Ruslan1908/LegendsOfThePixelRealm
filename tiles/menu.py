import pygame
import sys
from config import SCREEN_WIDTH, WHITE


# Minimalna klasa Button z komentarzami po polsku
class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x, self.y = pos
        self.font = font
        self.text_input = text_input
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(text_input, True, self.base_color) if text_input != "" else None
        self.rect = self.image.get_rect(center=pos)

    def update(self, screen):
        if self.text:
            screen.blit(self.text, self.text.get_rect(center=self.rect.center))
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


def get_font(size):
    """Funkcja zwraca czcionkę o określonym rozmiarze."""
    return pygame.font.Font("assets/fonts/font.ttf", size)


def character_selection(screen):
    """Funkcja obsługująca wybór postaci przez gracza."""
    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        title_text = get_font(45).render("Wybierz Swojego Rycerza", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
        screen.blit(title_text, title_rect)

        button_knight1 = Button(pygame.image.load("assets/buttons/knight1.png"), (200, 300), "", get_font(75),
                                (200, 200, 200), (255, 255, 255))
        button_knight2 = Button(pygame.image.load("assets/buttons/knight2.png"), (400, 300), "", get_font(75),
                                (200, 200, 200), (255, 255, 255))
        button_knight3 = Button(pygame.image.load("assets/buttons/knight3.png"), (600, 300), "", get_font(75),
                                (200, 200, 200), (255, 255, 255))

        for button in [button_knight1, button_knight2, button_knight3]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_knight1.checkForInput(mouse_pos):
                    return "knight1"
                if button_knight2.checkForInput(mouse_pos):
                    return "knight2"
                if button_knight3.checkForInput(mouse_pos):
                    return "knight3"

        pygame.display.update()


def main_menu(screen):
    """Funkcja wyświetlająca główne menu gry."""
    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        title_text = get_font(50).render("Legends Of The Pixel Realm", True, (100, 100, 100))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
        screen.blit(title_text, title_rect)

        play_button = Button(pygame.image.load("assets/buttons/play.png"), (SCREEN_WIDTH / 2, 250), "", get_font(75),
                             (200, 200, 200), (255, 255, 255))
        options_button = Button(pygame.image.load("assets/buttons/options.png"), (SCREEN_WIDTH / 2, 350), "",
                                get_font(75), (200, 200, 200), (255, 255, 255))
        quit_button = Button(pygame.image.load("assets/buttons/quit.png"), (SCREEN_WIDTH / 2, 450), "", get_font(75),
                             (200, 200, 200), (255, 255, 255))

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    player_choice = character_selection(screen)
                    print("Wybrano postać:", player_choice)
                    return  # Po wyborze postaci przechodzimy do rozgrywki
                if options_button.checkForInput(mouse_pos):
                    print("Opcje")
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()