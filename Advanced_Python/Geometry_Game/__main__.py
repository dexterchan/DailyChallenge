from __future__ import annotations
from .model import Rectangle, Point
from random import randint

if __name__ == "__main__":
    rectangle: Rectangle = Rectangle(
        lower_left=Point(x=randint(0, 9), y=randint(0, 9)),
        upper_right=Point(x=randint(10, 19), y=randint(10, 19))
    )
    print("Rectangle Coordinates:",
          str(rectangle))
    user_point: Point = Point(x=float(input("Guess X:")),
                              y=float(input("Guess Y:")))
    user_area: float = float(input("Guess rectangle area: "))
    print("Your point was inside rectange:",
          rectangle.check_point_inside(user_point))
    print("Your area was off by: ", rectangle.area - user_area)
