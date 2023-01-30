from ..point import Point
from .metric import Metric

class ManhattanDistance(Metric):
    """
    Euclidean distance
    """
    def calculate(self, point1: Point, point2: Point) -> float:
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)