from random import shuffle, random
from copy import copy
from .solver import Solver
from ..selection.selection import Selection
from ..crossover.crossover import Crossover
from ..mutation.mutation import Mutation
from ..fitness.fitness import Fitness


class GeneticAlgorithm(Solver):
    """
    Genetic algorithm with selection, crossover, and mutation
    """
    def __init__(
        self, crossover: Crossover, selection: Selection, mutation: Mutation, 
        sequence_length: int, fitness: Fitness, generation_size: int=10, 
        crossover_rate: float= 0.6, mutation_rate: float=0.01
    ):
        super().__init__()

        self.fitness = fitness
        self.crossover = crossover
        self.selection = selection
        self.mutation = mutation
        self.sequence_length = sequence_length
        self.generation_size = generation_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        self.generation = self.random_generation()
        self.fitness_scores = self.fitness.generate_scores(self.generation)
        self.sort_generation_fitness()

        self.current_score = self.fitness_scores[0]
        self.best_score = self.fitness_scores[0]
        self.current_state = self.generation[0]
        self.best_state = self.generation[0]
    
    def step(self):
        """
        Does one epoch of the algorithm
            - Selection
            - Crossover
            - Mutation
        """
        # Determine number of elitists and parents
        num_selections = int(self.generation_size * self.crossover_rate)
        num_selections += num_selections % 2
        num_elitists = self.generation_size - num_selections
        
        # Breed children via crossover
        parents = self.selection.select(self.generation, self.fitness_scores, num_selections)
        children = self.crossover.crossover(parents)
        elitists = self.generation[:num_elitists]
        self.generation = elitists + children

        # Mutate
        # Append instead of replace so elitists can be mutatated without being destroyed
        for i, sequence in enumerate(self.generation):
            random_number = random()
            if random_number < self.mutation_rate:
                self.generation.append(self.mutation.mutate(sequence))

        # Update generation and fitness scores
        self.fitness_scores = self.fitness.generate_scores(self.generation)
        self.sort_generation_fitness()

        # Only keep the first generation_size states
        self.generation = self.generation[:self.generation_size]
        self.fitness_scores = self.fitness_scores[:self.generation_size]

        # Update current epoch best sequence
        self.current_score = self.fitness_scores[0]
        self.current_state = self.generation[0]

        # Update best sequence
        if self.fitness.evaluate_state(self.current_state) > self.fitness.evaluate_state(self.best_state):
            self.best_state = copy(self.current_state)

    def random_generation(self) -> list[list[int]]:
        """
        Generates a random generation of length generation_size
        where each sequence has length sequence_length
        """
        sequence = [i for i in range(self.sequence_length)]
        new_generation = []
        for _ in range(self.generation_size):
            shuffle(sequence)
            new_generation.append(copy(sequence))
        return new_generation

    def sort_generation_fitness(self):
        """
        Sorts generation and fitness_scores by fitness_scores in desceneding order
        """
        self.fitness_scores, self.generation = zip(*sorted(zip(self.fitness_scores, self.generation), reverse=True))
        self.fitness_scores = list(self.fitness_scores)
        self.generation = list(self.generation)