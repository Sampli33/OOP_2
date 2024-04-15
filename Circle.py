class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = int(radius)
        Circle.all_circles.append(self)

    def area(self):
        circle_area = Circle.pi * self.radius**2
        return circle_area

    @staticmethod
    def total_area():
        sum_areas = 0
        for circle in Circle.all_circles:
            sum_areas += circle.area()
        return sum_areas

    def __str__(self):
        return f'{self.radius}'

    def __repr__(self):
        return self.__str__()
