from area.shape import Shape


class Oval(Shape):
    def __init__(self, s_radius, b_radius):
        self.ova_area = 0.0
        self.s_radius = s_radius
        self.b_radius = b_radius
        self.pi = 3.14

    def area(self):
        self.ova_area = self.pi * self.s_radius * self.b_radius
        return self.ova_area

    def __str__(self) -> str:
        return 'Oval Area of ' + str(self.s_radius) + ' U' + str(self.b_radius) + ' U :' + str(self.area())

