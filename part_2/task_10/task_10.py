'''
С помощью модификатора final можно обозначить метод, который закрыт для
переопределения в потомках.

Данный модификатор описан в PEP 591 – Adding a final qualifier to typing.
'''

from copy import deepcopy
from typing import TypeVar, final

T = TypeVar('T')


class General(object):

    # Конструктор
    # постусловие: создан новый объект
    def __init__(self, **kwargs) -> None: ...

    # запросы
    # глубокое копирование содержимого в другой объект
    @final
    def copy(self, other: T) -> None:
        other.__dict__ = deepcopy(self.__dict__)


class Any(General):

    # В случае попытки переопределить метод, получаем сообщение ниже.
    # Method "copy" cannot override final method defined in class "General"
    # Pylance task_10.py(16, 9): Final method
    def copy(self, other: T) -> None:
        other.__dict__ = self.__dict__.copy()

    # Важно! При этом практически переопределить метод можно.
    # Программа отработает без ошибки.
