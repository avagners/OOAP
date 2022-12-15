from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')
PowerSet = TypeVar('PowerSet', set)


# АТД HashTable
class AbsHashTable(ABC, Generic[T]):

    # Конструктор
    # постусловие: создана пустая хэш-таблица фиксированного размера
    def __init__(self, size: int) -> None: ...

    # Команды:
    # предусловие: в таблице есть свободные слота
    # постусловие: новое значение добавлено в таблицу
    @abstractmethod
    def put(self, value: T) -> None: ...
    # предусловие: в таблице есть запрашиваемое значение
    # постусловие: значение удалено из таблицы
    @abstractmethod
    def remove(self, value: T) -> None: ...

    # Запросы:
    @abstractmethod
    def find(self, value: T) -> bool: ...  # есть значение в таблице или нет
    @abstractmethod
    def size(self) -> int: ...  # кол-во заполненных слотов в таблице

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_put_status(self) -> int: ...  # успешно;
    # в таблице нет свободных слотов

    @abstractmethod
    def get_remove_status(self) -> int: ...  # успешно;
    # в таблице нет запрашиваемого значения


# АТД PowerSet
class AbsPowerSet(AbsHashTable):

    # Конструктор
    # постусловие: создано пустое множество фиксированного размера
    def __init__(self, size: int) -> PowerSet: ...

    # Запросы:
    # пересечение текущего множества с множеством set
    @abstractmethod
    def intersection(self, set: PowerSet) -> PowerSet: ...
    # объединение двух множеств
    @abstractmethod
    def union(self, set: PowerSet) -> PowerSet: ...
    # подмножество текущего множества из элементов, которые не входят set
    @abstractmethod
    def difference(self, set: PowerSet) -> PowerSet: ...
    # входят ли все элементы set в текущее множество
    @abstractmethod
    def issubset(self, set: PowerSet) -> bool: ...
