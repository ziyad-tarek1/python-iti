
# class Shape:
#     class Count:
#         shape_count = 0

#     def __init__(self, dimension1, dimension2):
#         self.dimension1 = dimension1
#         self.dimension2 = dimension2
#         Shape.Count.shape_count += 1  

#     def calc_area(self):
#         return self.dimension1 * self.dimension2  



class Shape:
        
    # class Count:
    shape_count = 0

    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2
        Shape.shape_count += 1  

    def calc_area(self):
        return self.dimension1 * self.dimension2  
