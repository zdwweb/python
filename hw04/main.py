import math as m


class Rectangle(object):
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, width=0):
        super().__init__(width, width)


class Ellipse(object):
    def __init__(self, a=0, b=0):  # a为椭圆长半轴，b为短半轴
        self.a = a
        self.b = b

    def area(self):
        return m.pi * self.a * self.b


class Circle(Ellipse):
    def __init__(self, radius=0):
        super().__init__(radius, radius)


def compute_area(shapes):
    return sum(shape.area() for shape in shapes)


def main():
    shapes = [Ellipse(10, 20), Square(15), Circle(5),
              Rectangle(20, 15), Circle(5), Square(15),
              Ellipse(10, 20)]
    total_area = compute_area(shapes)
    print("total_area:{0}".format(round(total_area, 2)))


main()
