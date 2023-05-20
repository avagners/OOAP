from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД Уровень игры (локация).
class Location(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан уровень игры
    def __init__(self) -> None: ...


# АТД Фабрика уровеней (локаций).
class AbstractLocationFactory(ABC, Generic[T]):

    # Статусы
    BUILD_LOCATION_NIL = 0  # build_location() не вызывался
    BUILD_LOCATION_OK = 1  # успешно создан объект типа Location
    BUILD_LOCATION_ERR = 2  # ошибка создания уровня

    # Конструктор
    # постусловие: создан уровень игры
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: создан объект типа Location
    @abstractmethod
    def build_location(self) -> Location: ...

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_build_location_status(self) -> int: ...  # успешно;
    # кол-во предметов достигло максимального значения;
