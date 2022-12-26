from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class A(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан объект размером size
    def __init__(self, size: int) -> None: ...

    # Команды:
    # предусловие: есть свободное место в A
    # постусловие: новое значение добавлено в A
    @abstractmethod
    def add(self, value: T) -> None: ...
    # предусловие: в A есть запрашиваемое значение
    # постусловие: значение value удалено из A
    @abstractmethod
    def delete(self, value: T) -> None: ...

    # Запросы:
    @abstractmethod
    def info(self) -> None: ...  # некоторая информация об объекте класса А


# Пример наследования и полиморфизма конструктора и метода
class B(A):

    # Конструктор
    # постусловие: создан объект размером size
    def __init__(self, size: int) -> None:
        super().__init__(size)

    # Запросы:
    @abstractmethod
    def info(self) -> None: ...  # другая информация об объекте класса B


# Пример композиции и полиморфизма
class C(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан объект с обязательными полями object_a, object_b
    def __init__(self, object_a: A, object_b: B) -> None: ...

    # Запросы:
    @abstractmethod
    def info(self) -> None: ...  # третья информация об объекте класса C
