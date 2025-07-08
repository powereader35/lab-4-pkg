from abc import ABC, abstractmethod

import math #(only in Circle)


class Shape(ABC):
    @abstractmethod
    def area(self):
        #"Compute area of the shape."
        None

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2
