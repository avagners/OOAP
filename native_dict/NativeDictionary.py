from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД NativeDictionary
class AbsNativeDictionary(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан ассоциативный массив
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: если ключа нет в массиве, то
    # новая пара ключ-значение добавлена в массив;
    # если ключ есть в массиве, то обновлено значение ключа
    @abstractmethod
    def put(self, key: T, value: T) -> None: ...
    # предусловие: в массиве есть запрашиваемый ключ
    # постусловие: пара "ключ-значение" удалена из массива
    @abstractmethod
    def remove(self, key: T) -> None: ...

    # Запросы:
    @abstractmethod
    def is_key(self, key: T) -> bool: ...  # есть ключ в массиве или нет
    @abstractmethod
    def size(self) -> int: ...  # кол-во пар "ключ-значение" в массиве
    # предусловие: запрашиваемый ключ есть в массиве
    @abstractmethod
    def get(self, key: T) -> T: ...  # получено значение по ключу

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_put_status(self) -> int: ...  # успешно добавлена новая пара
    # "ключ-значение"; успешно обновлено значение по ключу

    @abstractmethod
    def get_remove_status(self) -> int: ...  # успешно удалена пара
    # "ключ-значение"; в массиве нет запрашиваемого ключа

    @abstractmethod
    def get_get_status(self) -> int: ...  # успешно получено значение по ключу;
    # в массиве нет запрашиваемого ключа
