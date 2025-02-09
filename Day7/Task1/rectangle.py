
from shape import Shape

class Rectangle(Shape):
    
    rectangle_count = 0

    def __init__(self, length, width):
        super().__init__(length, width)
        Rectangle.rectangle_count += 1  
    def calc_area(self):
        return self.dimension1 * self.dimension2  
