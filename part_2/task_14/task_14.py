from typing import List, TypeVar, Union

T = TypeVar('T')


class General:
    pass


class Vector(General):

    def __init__(self, values: List[T]):
        self.values = values

    def __add__(self, other: "Vector[T]") -> Union["Vector[T]", None]:
        if len(self.values) != len(other.values):
            return None
        return Vector([x + y for x, y in zip(self.values, other.values)])
