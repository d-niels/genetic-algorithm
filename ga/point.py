from dataclasses import dataclass

@dataclass
class Point:
    """
    Simple class for keeping track of (x, y) coords
    """
    x: int
    y: int