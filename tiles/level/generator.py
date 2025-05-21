import random
import pygame
from level.dungeon_map import Room
from scipy.spatial import Delaunay
import networkx as nx


class Leaf:
    MIN_SIZE = 15  # Minimalny rozmiar liścia

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.room = None

    def split(self):
        """Dzieli liść na dwa mniejsze liście. Zwraca True, jeśli podział się powiódł."""
        if self.left or self.right:
            return False

        split_horizontally = random.choice([True, False])
        if self.width > self.height and self.width / self.height >= 1.25:
            split_horizontally = False
        elif self.height > self.width and self.height / self.width >= 1.25:
            split_horizontally = True

        max_size = (self.height if split_horizontally else self.width) - Leaf.MIN_SIZE
        if max_size <= Leaf.MIN_SIZE:
            return False

        split = random.randint(Leaf.MIN_SIZE, max_size)

        if split_horizontally:
            self.left = Leaf(self.x, self.y, self.width, split)
            self.right = Leaf(self.x, self.y + split, self.width, self.height - split)
        else:
            self.left = Leaf(self.x, self.y, split, self.height)
            self.right = Leaf(self.x + split, self.y, self.width - split, self.height)

        return True

    def create_room(self):
        """Tworzy pokój wewnątrz liścia z losowymi wymiarami."""
        room_width = random.randint(6, self.width - 2)
        room_height = random.randint(6, self.height - 2)
        room_x = random.randint(self.x + 1, self.x + self.width - room_width - 1)
        room_y = random.randint(self.y + 1, self.y + self.height - room_height - 1)
        self.room = Room(room_x, room_y, room_width, room_height)


def generate_dungeon(width, height, max_leaf_size=20):
    """
    Generuje lochy na podstawie metody BSP.
    Zwraca listę wygenerowanych pokoi.
    """
    root = Leaf(0, 0, width, height)
    leaves = [root]
    rooms = []

    did_split = True
    while did_split:
        did_split = False
        for leaf in leaves[:]:
            if not leaf.left and not leaf.right:
                if leaf.width > max_leaf_size or leaf.height > max_leaf_size or random.random() > 0.8:
                    if leaf.split():
                        leaves.append(leaf.left)
                        leaves.append(leaf.right)
                        did_split = True

    for leaf in leaves:
        if not leaf.left and not leaf.right:
            leaf.create_room()
            if leaf.room:
                rooms.append(leaf.room)

    return rooms


def connect_rooms(rooms):
    """
    Łączy pokoje przy pomocy triangulacji Delaunay oraz MST,
    generując połączenia korytarzami.
    """
    points = [room.center for room in rooms]
    tri = Delaunay(points)

    edges = set()
    for simplex in tri.simplices:
        for i in range(3):
            edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
            edges.add(edge)

    graph = nx.Graph()
    for edge in edges:
        p1, p2 = points[edge[0]], points[edge[1]]
        distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        graph.add_edge(edge[0], edge[1], weight=distance)

    mst = nx.minimum_spanning_tree(graph)
    final_edges = list(mst.edges)

    extra_edges = list(edges - set(mst.edges))
    random.shuffle(extra_edges)
    final_edges += extra_edges[:len(extra_edges) // 4]

    return [(points[a], points[b]) for a, b in final_edges]


def create_corridors(surface, connections, tile_size=10):
    """
    Rysuje korytarze między pokojami na podanej powierzchni (surface).
    """
    for (x1, y1), (x2, y2) in connections:
        x1, y1 = int(x1 * tile_size), int(y1 * tile_size)
        x2, y2 = int(x2 * tile_size), int(y2 * tile_size)
        if random.random() > 0.5:
            pygame.draw.line(surface, (180, 180, 180), (x1, y1), (x2, y1), 5)
            pygame.draw.line(surface, (180, 180, 180), (x2, y1), (x2, y2), 5)
        else:
            pygame.draw.line(surface, (180, 180, 180), (x1, y1), (x1, y2), 5)
            pygame.draw.line(surface, (180, 180, 180), (x1, y2), (x2, y2), 5)