from __future__ import annotations
from pydantic import BaseModel
import math


class Point(BaseModel):
    x: float
    y: float

    def distance(self, point: Point) -> float:
        return math.sqrt(pow((self.x - point.x), 2) + pow(self.y - point.y))

    def fall_into_rectangle(self, rectangle: Rectangle) -> bool:
        return rectangle.lower_left.x < self.x < rectangle.upper_right.x \
            and rectangle.lower_left.y < self.y < rectangle.upper_right.y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"


class Rectangle(BaseModel):
    lower_left: Point
    upper_right: Point

    @classmethod
    def create(cls, lower_left: Point, upper_right: Point) -> Rectangle:
        instance: Rectangle = cls(
            lower_left=lower_left, upper_right=upper_right
        )
        if not instance.validate():
            raise Exception("invalid rectangle")
        return instance

    def validate(self) -> bool:
        if self.lower_left.x >= self.upper_right.x:
            return False
        if self.lower_left.y >= self.upper_right.y:
            return False
        return True

    def check_point_inside(self, point: Point) -> bool:
        if (self.lower_left.x < point.x < self.upper_right.x) \
                and (self.lower_left.y < point.y < self.upper_right.y):
            return True
        else:
            return False

    @property
    def area(self) -> float:
        return (self.upper_right.x - self.lower_left.x) * (self.upper_right.y - self.lower_left.y)

    def __str__(self) -> str:
        return f"{str(self.lower_left) } and {str(self.upper_right)}"
