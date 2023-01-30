class Solver():
    """
    Solver for the TSP problem
    Must implement a step function
    """
    def __init__(self):
        # Recorded data
        self.current_state: list[int] = [] 
        self.best_state: list[int] = []
        self.current_score: float = 0
        self.best_score: float = 0
        self.finished: bool = False
    
    def step(self):
        raise NotImplementedError()
