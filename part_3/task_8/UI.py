from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД Элемент пользовательского интерфейса.
class UIElement(ABC, Generic[T]):

    # Статусы
    DELETE_NIL = 0  # delete() не вызывался
    DELETE_OK = 1  # элемент успешно удален
    DELETE_ERR = 2  # элемент отсутствует

    # Конструктор
    # постусловие: создан элемент UI
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: есть элемент UI
    # постусловие: элемент удален
    @abstractmethod
    def delete(self) -> None: ...

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_delete_status(self) -> int: ...  # успешно; ошибка;


# АТД Экран пользовательского интерфейса.
class UIScreen(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан экран UI
    def __init__(self) -> None: ...
