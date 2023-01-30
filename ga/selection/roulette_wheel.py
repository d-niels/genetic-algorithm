from random import choices
from .selection import Selection

class RouletteWheel(Selection):
    def __init__(self):
        pass

    def select(self, generation: list[list[int]], fitness_scores: list[float], num_selections: int) -> list[list[int]]:
        fitness_probability = []
        sum_fitness = sum(fitness_scores)
        for f in fitness_scores:
            fitness_probability.append(f / sum_fitness)
        
        selections = choices(
            generation,
            weights = fitness_probability,
            k = num_selections
        )
        
        return list(selections)