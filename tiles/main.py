import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from menu import main_menu


# Główna funkcja gry – punkt wejścia
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("LegendsOfThePixelRealm")
    clock = pygame.time.Clock()

    # Uruchomienie menu głównego
    main_menu(screen)

    # Pętla gry (dalsze moduły rozgrywki mogą być tutaj integrowane)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

