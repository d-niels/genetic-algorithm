from .crossover import Crossover
from random import randint
from copy import copy

class TwoPoint(Crossover):
    """
    Crossover where 2 points are picked and everything between
    those points are crossed over
    """
    def __init__(self, crossover_size: int=None):
        self.crossover_size = crossover_size

    def crossover(self, parents: list[list[int]]) -> list[list[int]]:
        """
        Splits the parents into pairs and uses them for crossover
        """
        children = []
        for i in range(0, len(parents), 2):
            child1, child2 = self._crossover(parents[i], parents[i+1])
            children += [child1, child2]
        return children

    def _crossover(self, sequence1: list[int], sequence2: list[int]) -> tuple[list[int], list[int]]:
        """
        Chooses the indices (left, right) inclusive to swap on 
        then call a function to swap them
        This is broken into two functions for debugging purposes
        """
        # Get the indices to swap on
        left = randint(0, len(sequence1)-2)
        right = randint(left+1, len(sequence1)-1)

        if self.crossover_size:
            left = randint(0, len(sequence1)-1-self.crossover_size)
            right = left + self.crossover_size
        
        return self.cross(sequence1, sequence2, left, right)

    def cross(self, sequence1: list[int], sequence2: list[int], left: int, right: int) -> tuple[list[int], list[int]]:
        """
        Edit non-swapped points to resolve constraints
        In the segment that wasn't swapped, find any numbers that are in the swapped
        segment and remove them. Then find the numbers that are missing from the organism.
        Fill in the holes in the organism with the missing numbers in the order they show up
        in the parent
        e.g.
        
        organism     = [0, 3, 1, 2, 5, 6, 7, 4]
        swapped      = [0, 3, 0, 2, 4, 1, 7, 4]
                              ^--------^
                             left    right
                            swapped portion

        repeated numbers: 0, 4
        missing numbers:  5, 6
        since 5 comes before 6 in the parent
        
        new_organism = [3, 5, 0, 2, 4, 1, 6, 7]
        """

        # Copy the solutions
        new_sequence1 = copy(sequence1)
        new_sequence2 = copy(sequence2)

        # Swap
        new_sequence1[left:right+1] = sequence2[left:right+1]
        new_sequence2[left:right+1] = sequence1[left:right+1]

        # Resolve sequences
        r_left = left
        r_right = -(len(sequence1)-right-1)
        if r_right == 0:
            r_right = len(sequence1)

        # Resolve solution1
        swapped = new_sequence1[left:right+1]
        not_swapped = [s for s in sequence1 if s not in swapped]
        new_sequence1[:left] = not_swapped[:r_left]
        new_sequence1[right+1:] = not_swapped[r_right:]

        # Resolve solution2
        swapped = new_sequence2[left:right+1]
        not_swapped = [s for s in sequence2 if s not in swapped]
        new_sequence2[:left] = not_swapped[:r_left]
        new_sequence2[right+1:] = not_swapped[r_right:]

        return new_sequence1, new_sequence2