
from shape import Shape
from circle import Circle
from rectangle import Rectangle


square = Shape(2, 3)  
square2 = Shape(2, 3)  


circle = Circle(5)  
circle2 = Circle(6)  

rectangle = Rectangle(4, 6)  

print(f"area of square: {square.calc_area()}")  
print(f"area of circle: {circle.calc_area()}")
print(f"area of rectangle: {rectangle.calc_area()}")



print(f"total Shapes: {Shape.shape_count}")
print(f"total Circles: {Circle.circle_count}")
print(f"total Rectangles: {Rectangle.rectangle_count}")
