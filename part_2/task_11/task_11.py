import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from typing import final

from task_9.task_9 import Any


class FirstClass(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class SecondClass(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


@final
class NoneType(FirstClass, SecondClass):

    @final
    def __new__(cls, **kwargs):
        return None


if __name__ == '__main__':
    a: FirstClass = FirstClass(content=1)
    b: SecondClass = SecondClass(content=2)
    x: Any = NoneType()

    for obj in [a, b, x]:
        if obj is None:
            continue
        print(obj.attributes())
