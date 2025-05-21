import pygame


class Inventory:
    def __init__(self):
        # Lista przechowująca przedmioty w ekwipunku
        self.items = []

    def add_item(self, item):
        """Dodaje przedmiot do ekwipunku."""
        self.items.append(item)
        print(f"Dodano przedmiot: {item}")

    def use_item(self, item_index):
        """Używa przedmiotu z ekwipunku."""
        if 0 <= item_index < len(self.items):
            item = self.items.pop(item_index)
            print(f"Użyto przedmiot: {item}")
            return item
        return None

    def draw(self, surface, font):
        """Rysuje zawartość ekwipunku na ekranie."""
        x = 10
        y = surface.get_height() - 50
        for item in self.items:
            text = font.render(str(item), True, (255, 255, 255))
            surface.blit(text, (x, y))
            x += 100