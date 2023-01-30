from .selection import Selection
from ..point import Point

class Rank(Selection):
    def __init__(self):
        pass

    def select(node_coords: list[Point], fitness: list[float], num_selections: int) -> list[list[int]]:
        return node_coords[:num_selections]