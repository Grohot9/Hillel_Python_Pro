class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x=x, y=y)
        self.radius = radius

    def __contains__(self, point: Point) -> bool:
        if ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 2 <= self.radius:
            return True
        return False
