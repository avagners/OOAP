from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


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
    # предусловие: в таблице есть запрашиваемое значение
    @abstractmethod
    def get(self, value: T) -> T: ...  # значение из таблицы
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

    @abstractmethod
    def get_get_status(self) -> int: ...  # успешно;
    # в таблице нет запрашиваемого значения
