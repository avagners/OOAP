import pickle
from copy import deepcopy
from typing import TypeVar, Union, final

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
    def clone(self) -> 'General':
        return deepcopy(self)

    @final
    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @final
    @staticmethod
    def deserialize(serialized_obj: bytes) -> 'General':
        return pickle.loads(serialized_obj)

    # является ли тип текущего объекта типом classtype
    @final
    def is_type(self, classtype) -> bool:
        return type(self) == classtype

    # получено класс объекта
    @final
    def type(self):
        return self.__class__

    # наглядное представление содержимого объекта в текстовом формате
    @final
    def attributes(self) -> str:
        return f'attributes: {self.__dict__}'

    # сравнение объектов (включая глубокий вариант)
    @final
    def __eq__(self, other: T) -> bool:
        return self.__dict__ == other.__dict__

    # присваивание
    @final
    @staticmethod
    def assignment_attempt(target: 'General',
                           source: 'General') -> Union['General', 'NoneType']:
        if target.is_type(source.type()):
            return source
        return NoneType()


class Any(General):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__dict__ = kwargs


class FirstClass(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class SecondClass(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


# Замыкание иерархии
@final
class NoneType(FirstClass, SecondClass):

    @final
    def __new__(cls, **kwargs):
        return None
