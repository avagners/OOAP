from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


# АТД Показатель персонажа.
# Его будут наследовать классы для таких показателей как голод, сытость.
class CharacterIndicator(ABC, Generic[T]):

    # Статусы
    DECREASE_NIL = 0  # decrease() не вызывался
    DECREASE_OK = 1  # показатель успешно уменьшился на n-единиц
    DECREASE_ERR = 2  # показатель меньше нуля

    INCREASE_NIL = 0  # increase() не вызывался
    INCREASE_OK = 1  # показатель успешно увеличился на n-единиц
    INCREASE_ERR = 2  # показатель больше 100%

    # Конструктор
    # постусловие: создано число, символизирующее кол-во показателя
    # (по-умолчанию эквивалентно 100%)
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: показатель больше нуля
    # постусловие: уменьшает показатель на n-единиц
    @abstractmethod
    def decrease(self, n: int) -> None: ...

    # предусловие: показатель меньше 100%
    # постусловие: увеличивает показатель на n-единиц (макс. 100%)
    @abstractmethod
    def increase(self, n: int) -> None: ...

    # Запросы:
    @abstractmethod
    def get_info(self) -> int: ...  # текущее состояние показателя

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_decrease_status(self) -> int: ...  # успешно;
    # показатель меньше нуля;
    @abstractmethod
    def get_increase_status(self) -> int: ...  # успешно;
    # показатель больше 100%;


# АТД Персонаж.
# Его будут наследовать классы персонажей.
class Character(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан объект, который содержит поля
    # - индикаторы персонажа CharacterIndicator
    # - имя персонажа String
    def __init__(self) -> None: ...

    # Запросы:
    @abstractmethod
    def get_name(self) -> str: ...  # имя персонажа


# АТД Враг.
# Его будут наследовать классы врагов.
class Enemy(ABC, Generic[T]):

    # Статусы
    HIT_NIL = 0  # hit() не вызывался
    HIT_OK = 1  # успешно нанесен урон на n-единиц
    HIT_ERR = 2  # показатель меньше нуля

    # Конструктор
    # постусловие: создан объект, который содержит поля
    # - индикаторы персонажа CharacterIndicator
    # - имя врага String
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: значение показателя больше нуля
    # постусловие: уменьшает показатель на n-единиц
    def hit(self, n: int) -> None: ...

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_hit_status(self) -> int: ...  # успешно;
    # показатель меньше нуля;


# АТД Фабрика Врагов.
# Его можно наследовать при создании класса фабрики врагов.
class AbstractEnemyFactory(ABC, Generic[T]):

    # Статусы
    BUILD_ENEMY_NIL = 0  # build() не вызывался
    BUILD_ENEMY_OK = 1  # успешно создан объект типа Enemy
    BUILD_ENEMY_ERR = 2  # создано максимальное кол-во врагов на уровне

    # Конструктор
    # постусловие: создан объект врага Enemy
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: создан объект типа Enemy
    @abstractmethod
    def build_enemy(self) -> Enemy: ...

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_build_enemy_status(self) -> int: ...  # успешно;
    # кол-во врагов достигло максимального значения;
