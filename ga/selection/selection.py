from ..point import Point
from random import random, choices

class Selection():
    def __init__(self):
        pass
    
    def select(self, generation: list[list[int]], fitness: list[float], num_selections: int) -> list[list[int]]:
        raise NotImplementedError()