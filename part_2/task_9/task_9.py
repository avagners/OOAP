import pickle
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

    # создает новый объект с глубоким копированием исходного объекта
    @final
    def clone(self) -> T:
        return deepcopy(self)

    @final
    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @final
    @staticmethod
    def deserialize(serialized_obj: bytes) -> T:
        return pickle.loads(serialized_obj)

    # является ли тип текущего объекта типом classtype
    @final
    def is_type(self, classtype) -> bool:
        return type(self) == classtype

    # получено название класса объекта
    @final
    def type(self):
        return self.__class__.__name__

    # наглядное представление содержимого объекта в текстовом формате
    @final
    def print_attributes(self) -> str:
        return f'attributes: {self.__dict__}'

    # сравнение объектов (включая глубокий вариант)
    @final
    def __eq__(self, other: T) -> bool:
        return self.__dict__ == other.__dict__


class Any(General):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__dict__ = kwargs
