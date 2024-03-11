class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        if isinstance(other_point, Point):
            return Point(self.x + other_point.x, self.y + other_point.y)
        else:
            raise TypeError("Unsupported operand type. Must be a Point.")

# Creating two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using the + operator with Point objects
result = point1 + point2

# Displaying the result
print(f"Result: ({result.x}, {result.y})")
