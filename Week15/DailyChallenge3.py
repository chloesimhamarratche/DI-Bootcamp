import math


# ============================================================
# Daily Challenge : Circle
# ============================================================

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.diameter}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("You can only add a Circle with another Circle")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        raise TypeError("You can only compare a Circle with another Circle")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        raise TypeError("You can only compare a Circle with another Circle")


# ============================================================
# Test the code
# ============================================================

circle1 = Circle(radius=5)
circle2 = Circle(diameter=20)
circle3 = Circle(radius=3)
circle4 = Circle(radius=5)

print("===== Circle 1 =====")
print(circle1)
print("Area:", circle1.area())
print()

print("===== Circle 2 =====")
print(circle2)
print("Area:", circle2.area())
print()

print("===== Add two circles =====")
circle5 = circle1 + circle2
print(circle5)
print()

print("===== Compare circles =====")
print(circle1 > circle3)   # True
print(circle1 > circle2)   # False
print(circle1 == circle4)  # True
print()

print("===== Sort circles =====")
circles = [circle1, circle2, circle3, circle4, circle5]

sorted_circles = sorted(circles)

for circle in sorted_circles:
    print(circle)
