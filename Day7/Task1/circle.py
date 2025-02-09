
from shape import Shape

class Circle(Shape):
    circle_count = 0

    def __init__(self, radius):
        super().__init__(radius, radius)
        Circle.circle_count += 1  

    def calc_area(self):
        return 3.14159 * self.dimension1 * self.dimension2  
