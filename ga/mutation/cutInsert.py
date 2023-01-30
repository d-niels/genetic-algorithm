from copy import copy
from random import randint
from .mutation import Mutation

class CutInsert(Mutation):
    def __init__(self, cut_size: int=None):
        self.cut_size = cut_size
    
    def mutate(self, state: list[int]) -> list[int]:
        """
        Performs a mutation by cutting a segment from the list and pastes in somewhere else
        """
        # If the cut size is pre determined, use that
        # Otherwise generate a random cut size
        cut_size = randint(1, len(state)-1)
        if self.cut_size:
            cut_size = self.cut_size

        # Determine the indices for the cut and the paste location
        left = randint(0, len(state)-cut_size)
        right = left + cut_size
        new = randint(0, len(state)-cut_size)
        while new == left:
            new = randint(0, len(state)-cut_size)

        # Perform the cut and paste and return the new state
        return self._mutate(state, left, right, new)
    
    def _mutate(self, state: list[int], left: int, right: int, new: int) -> list[int]:
        """
        Performs a mutation
            Cut the portion between the left and right index (inclusive)
            Insert it back into the remaining list at the new index
        """
        cut = state[left:right]
        remaining = copy(state)
        for _ in range(left, right):
            remaining.pop(left)
        left_state = remaining[:new]
        right_state = remaining[new:]
        return left_state + cut + right_state
