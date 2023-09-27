from area.shape import Shape


class Cylinder(Shape):
    def __init__(self, radius, height):
        self.cyl_area = 0.0
        self.radius = radius
        self.height = height
        self.pi = 3.14

    def area(self):
        self.cyl_area = 2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2
        return self.cyl_area

    def __str__(self) -> str:
        return 'Cylinder Area of ' + str(self.radius) + ' U' + str(self.height) + ' U :' + str(self.area())