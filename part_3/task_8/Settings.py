from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД Пользовательские настройки.
class AbstractSettings(ABC, Generic[T]):

    CHANGE_NIL = 0  # change() не вызывался
    CHANGE_OK = 1  # успешно обновлено значение по ключу
    CHANGE_ERR = 2  # ключа нет в словаре

    # Конструктор
    # постусловие: создан словарь с настройками
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: ключ с настройкой есть в словаре
    # постусловие: значение настройки изменено по ключу
    @abstractmethod
    def change(self, key: str, value: T) -> None: ...

    # Запросы:
    @abstractmethod
    def is_key(self, key: str) -> bool: ...  # есть ключ в массиве или нет

    # предусловие: запрашиваемый ключ есть в массиве
    @abstractmethod
    def get(self, key: str) -> T: ...  # получено значение по ключу

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_change_status(self) -> int: ...  # обновлено значение по ключу
    # ключ отстутствует;


# АТД Игровой движок.
# Интерфейс для взимодествия с игровым движком
class Engine():

    # Конструктор
    # постусловие: создан объект игрового движка
    def __init__(self) -> None: ...
