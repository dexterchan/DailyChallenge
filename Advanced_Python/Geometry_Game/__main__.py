from __future__ import annotations
from .model import Rectangle, Point
from random import randint

if __name__ == "__main__":
    rectangle: Rectangle = Rectangle(
        lower_left=Point(x=randint(0, 9), y=randint(0, 9)),
        upper_right=Point(x=randint(10,19), y=randint(10, 19))
    )
    print("Rectangle Coordinates:",
          str(rectangle))
    user_point: Point = Point(x=float(input("Guess X:")),
                              y=float(input("Guess Y:")))
    print("Your point was inside rectange:", rectangle.check_point_inside(user_point))
    # r = Rectangle.create(
    #     lower_left=Point(x=0,y=0),
    #     upper_right=Point(x=2,y=9)
    # )
    #
    # print(r.validate())
    # print(r.check_point_inside(point=Point(x=1, y=1)))
    # print(r.check_point_inside(point=Point(x=1, y=10)))
