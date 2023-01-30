from copy import copy
from random import shuffle
from .solver import Solver
from ..fitness import Fitness

class Random(Solver):
    """
    Solver that tries every possible solution once
    """
    def __init__(self, sequence_length: int, fitness: Fitness):
        super().__init__()

        self.fitness = fitness
        self.sequence_length = sequence_length
        self.current_state = [i for i in range(sequence_length)]
        self.best_state = [i for i in range(sequence_length)]
        self.current_score = self.fitness.evaluate_state(self.current_state)
        self.best_score = self.current_score
    
    def step(self):
        shuffle(self.current_state)
        score = self.fitness.evaluate_state(self.current_state)
        if score > self.best_score:
            self.best_score = score
            self.best_state = copy(self.current_state)
    

