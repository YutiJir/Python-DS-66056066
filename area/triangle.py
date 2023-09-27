from area.shape import Shape


class Triangle(Shape):
    def __init__(self, width, height):
        self.tri_area = 0.0
        self.width = width
        self.height = height
        self.half = 0.5

    def area(self):
        self.tri_area = self.half * self.width * self.height
        return self.tri_area

    def __str__(self) -> str:
        return 'Triangle Area of ' + str(self.width) + ' U' + str(self.height) + ' U :' + str(self.area())