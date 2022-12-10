class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x=x, y=y)
        self.radius = radius

    def contains(self, point: Point) -> bool:
        print(self.x, self.y, self.radius, point.x, point.y)
        if ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 2 <= self.radius:
            return True
        return False
