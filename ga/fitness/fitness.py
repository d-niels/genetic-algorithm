class Fitness():
    """
    Class used for calculating the fitness score for
    each sequence in a generation
    """
    def __init__(self):
        pass

    def generate_scores(self, generation: list[list[int]]) -> float:
        scores = []
        for state in generation:
            scores.append(self.evaluate(state))
        return scores
    
    def evaluate_state(self, state: list[int]) -> float:
        raise NotImplementedError()