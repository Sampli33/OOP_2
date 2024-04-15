class Circle:
    """
    The `Circle` class represents a circle with a given radius in a two-dimensional plane.

    Attributes:
    radius (int): The radius of the circle.
    all_circles (list): A list to store all circle objects created.
    pi (float): A constant representing the value of pi (3.1415).

    Methods:
    __init__(radius=1): Initializes a new `Circle` object with the provided radius.
    area(): Calculates and returns the area of the circle.
    total_area(): Calculates and returns the total area of all circles created.
    __str__(): Returns a string representation of the circle's radius.
    __repr__(): Returns a string representation of the circle's radius.
    """

    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        """
        Initializes a new `Circle` object with the provided radius.

        Parameters:
        radius (int, optional): The radius of the circle (default is 1).
        """
        self.radius = int(radius)
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        float: The area of the circle.
        """
        circle_area = Circle.pi * self.radius**2
        return circle_area

    @staticmethod
    def total_area():
        """
        Calculates and returns the total area of all circles created.

        Returns:
        float: The total area of all circles.
        """
        sum_areas = 0
        for circle in Circle.all_circles:
            sum_areas += circle.area()
        return sum_areas

    def __str__(self):
        """
        Returns a string representation of the circle's radius.

        Returns:
        str: A string representation of the circle's radius.
        """
        return f'{self.radius}'

    def __repr__(self):
        """
        Returns a string representation of the circle's radius.

        Returns:
        str: A string representation of the circle's radius.
        """
        return self.__str__()
