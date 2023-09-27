# area_calc.py
from area.rectangle import Rect
from area.square import Square
from area.circle import Circle
from area.oval import Oval
from area.triangle import Triangle
from area.cylinder import Cylinder

if __name__ == '__main__':
    sq1 = Square(5)
    print(sq1)
    print(sq1.area())

    rect1 = Rect(5, 10)
    rect2 = Rect(7, 9)
    print(rect1)
    print(rect2)

    cr1 = Circle(5)
    print(cr1)
    print(cr1.area())

    ov1 = Oval(5,6)
    print(ov1)
    print(ov1.area())

    tr1 = Triangle(5,6)
    print(tr1)
    print(tr1.area())

    cy1 = Cylinder(5,6)
    print(cy1)
    print(cy1.area())


#%%
