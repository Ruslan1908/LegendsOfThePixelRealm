# Definicja klasy Room reprezentującej pokój w generowanych lochach

class Room:
    def __init__(self, x, y, width, height):
        self.x = x  # Pozycja X pokoju
        self.y = y  # Pozycja Y pokoju
        self.width = width  # Szerokość pokoju
        self.height = height  # Wysokość pokoju

    @property
    def center(self):
        """Zwraca środek pokoju jako krotkę (x, y)."""
        return (self.x + self.width // 2, self.y + self.height // 2)

    def intersects(self, other):
        """Sprawdza, czy pokój przecina się z innym pokojem."""
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)