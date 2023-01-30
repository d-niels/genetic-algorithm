from ..point import Point

class Metric():
    """
    Metric used to evaluate a path
    """
    def calculate(self, point1: Point, point2: Point) -> float:
        """
        Function for calculating the metric between 2 Points
        """
        raise NotImplementedError()

    def evaluate_sequence(self, node_coords: list[Point]) -> float:
        """
        Function that calculates the metric over a whole path of Points
        """
        aggregate = 0
        for i in range(len(node_coords)-1):
            aggregate += self.calculate(node_coords[i], node_coords[i+1])
        return aggregate
    
    def create_matrix(self, node_coords: list[Point]) -> list[list[float]]:
        """
        Creates a matrix that contains the metric between every
        possible pair of points
        """
        size = len(node_coords)

        # Create a matrix of zeros
        d_matrix = []
        for _ in range(size):
            d_matrix.append([0] * size)

        # Fill in the matrix
        for i in range(size):
            for j in range(i, size):
                val = self.calculate(node_coords[i], node_coords[j])
                d_matrix[i][j] = val
                d_matrix[j][i] = val
        
        return d_matrix
