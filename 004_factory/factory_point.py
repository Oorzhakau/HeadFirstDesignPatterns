from math import sin, cos


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    class PointFactory:
        def new_cartesian_point(self, x: int, y: int):
            return Point(x=x, y=y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()

    def __str__(self):
        return f"<Point x={self.x} y={self.y}>"


if __name__ == "__main__":
    p1 = Point(2, 3)
    print(p1)
    p2 = Point.factory.new_cartesian_point(4, 3)
    print(p2)
