from ..point import Point
from .metric import Metric

class EuclideanDistance(Metric):
    """
    Euclidean distance
    """
    def calculate(self, point1: Point, point2: Point) -> float:
        return ((point1.x - point2.x)**2 + 
                (point1.y - point2.y)**2)**0.5