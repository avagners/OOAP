from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar('T')


# АТД Игровой предмет.
class Item(ABC, Generic[T]):

    # Статусы
    DELETE_NIL = 0  # delete() не вызывался
    DELETE_OK = 1  # предмет успешно удален
    DELETE_ERR = 2  # ошибка удаления предмета

    # Конструктор
    # постусловие: создан игровой предмет:
    # - id предмета
    # - спрайт объекта (путь к изображению предмета)
    # - position - координаты предмета на экране
    # - cost - стоимость предмета
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: предмет удален с карты
    @abstractmethod
    def delete(self) -> None: ...

    # Запросы:
    @abstractmethod
    def get_info(self) -> dict: ...  # информация о предмете

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_delete_status(self) -> int: ...  # успешно; ошибка;


# АТД Фабрика предметов.
class AbstractItemFactory(ABC, Generic[T]):

    # Статусы
    BUILD_ITEM_NIL = 0  # build_item() не вызывался
    BUILD_ITEM_OK = 1  # успешно создан объект типа Item
    BUILD_ITEM_ERR = 2  # создано максимальное кол-во предметов на уровне

    # Конструктор
    # постусловие: создан объект врага Item
    def __init__(self) -> None: ...

    # Команды:
    # постусловие: создан объект типа Item
    @abstractmethod
    def build_item(self) -> Item: ...

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_build_item_status(self) -> int: ...  # успешно;
    # кол-во предметов достигло максимального значения;


# АТД Магазин.
class Store(ABC, Generic[T]):

    # Статусы
    BUY_NIL = 0  # buy() не вызывался
    BUY_OK = 1  # успешная покупка
    BUY_ERR = 2  # магазин пуст

    # Конструктор
    # постусловие: создан список объектов типа Item
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: предмет есть в магазине и
    # есть свободное место в хранилище,
    # есть достоточное кол-во монет;
    # постусловие: предмет удален из магазина
    # и помещен в хранилище персонажа;
    @abstractmethod
    def buy(self, item: Item) -> None: ...

    # Запросы:
    @abstractmethod
    def get_items(self) -> List[Item]: ...  # список товаров в магазине

    @abstractmethod
    def check_item(self, item_type: Item) -> bool: ...  # наличие предмета

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_buy_status(self) -> int: ...  # успешно;
    # предмета нет в магазине или нет места в хранилище;


# АТД Хранилище предметов персонажа.
class Storage(ABC, Generic[T]):

    # Статусы
    DELETE_ITEM_NIL = 0  # delete_item() не вызывался
    DELETE_ITEM = 1  # предмет успешно удален из хранилища
    DELETE_ITEM_ERR = 2  # предмета нет в хранилище

    ADD_ITEM_NIL = 0  # add_item() не вызывался
    ADD_ITEM_OK = 1  # предмет успешно добавлен в хранилища
    ADD_ITEM_ERR = 2  # нет свободного места в хранилище

    SELL_ITEM_NIL = 0  # sell_item() не вызывался
    SELL_ITEM_OK = 1  # предмет успешно продан
    SELL_ITEM_ERR = 2  # предмета нет в хранилище

    # Конструктор
    # постусловие: создан список объектов типа Item
    def __init__(self) -> None: ...

    # Команды:
    # предусловие: есть предмет в хранилище;
    # постусловие: предмет удален из хранилища;
    @abstractmethod
    def delete_item(self, item: Item) -> None: ...

    # предусловие: есть свободное место в хранилище;
    # постусловие: предмет добавлен в хранилище;
    @abstractmethod
    def add_item(self, item: Item) -> None: ...

    # предусловие: есть предмет в хранилище;
    # постусловие: предмет удален из хранилища,
    # предмет перемещен в магазин,
    # увеличено кол-во монет в показателях персонажа;
    @abstractmethod
    def sell_item(self, item: Item) -> None: ...

    # Запросы:
    @abstractmethod
    def get_items(self) -> List[Item]: ...  # список предметов в хранилище

    # Дополнительные запросы:
    # запросы статусов (возможные значения статусов)
    @abstractmethod
    def get_delete_item_status(self) -> int: ...  # успешно;
    # предмета нет в хранилище;
    @abstractmethod
    def get_add_item_status(self) -> int: ...  # успешно;
    # нет свободного места в хранилище;
    @abstractmethod
    def get_sell_item_status(self) -> int: ...  # успешно;
    # предмета нет в хранилище;
