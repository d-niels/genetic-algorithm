from . import Fitness
from ..metrics.metric import Metric
from ..point import Point

class TSP(Fitness):
    """
    Fitness scoring for the Traveling Salesperson Problem
    Distance between every point in a sequence
    """
    def __init__(self, metric: Metric, node_coords: list[Point]):
        self.metric = metric
        self.node_coords = node_coords
    
    def generate_scores(self, generation: list[list[int]]) -> list[float]:
        """
        Fitness score is 1 / distance of sequence
        This is so shorter distances have higher fitness scores
        """
        fitness_scores = []
        for sequence in generation:
            fitness_scores.append(self.evaluate_state(sequence))
        sum_fitness = sum(fitness_scores)
        return [f / sum_fitness for f in fitness_scores]
    
    def evaluate_state(self, sequence: list[int]) -> float:
        """
        Distance between every point in a sequence
        """
        new_sequence = [self.node_coords[0]] + [self.node_coords[i+1] for i in sequence] + [self.node_coords[-1]] + [self.node_coords[0]]
        return 1 / self.metric.evaluate_sequence(new_sequence)