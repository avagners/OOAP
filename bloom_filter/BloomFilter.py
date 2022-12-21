from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД BloomFilter
class AbsBloomFilter(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан фильтр Блюма с битовым массивом размером size
    def __init__(self, size: int) -> None: ...

    # Команды:
    # постусловие: новое значение добавлено в фильтр Блюма
    @abstractmethod
    def add(self, value: T) -> None: ...

    # Запросы:
    # есть ли значение в фильтре Блюма
    def is_value(self, value: T) -> bool: ...
