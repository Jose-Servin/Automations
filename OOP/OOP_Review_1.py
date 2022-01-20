# https://www.youtube.com/watch?v=MBbVq_FIYDA&ab_channel=BroCode


class Shape():

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        return self.width * self.length

class Cube(Shape):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height 

    def calculate_volume(self):
        return self.length * self.width * self.height


